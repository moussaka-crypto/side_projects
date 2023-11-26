package main

import (
	"log"
	"net/http"
	"sync"

	"github.com/gorilla/websocket"
)

var (
	// HTTP-requests in eine persistente Websocket Verbindung zu "upgraden"
	websocketUpgrader = websocket.Upgrader{
		ReadBufferSize:  1024,
		WriteBufferSize: 1024,
	}
)

// Referenzen zu allen registrierten Clients,
type Managment struct {
	clients ClientList
	sync.RWMutex
}

// initalize all the values inside the manager
func NewManager() *Managment {
	return &Managment{
		clients: make(ClientList),
	}
}

// erlaubt Verbindungen bzw. fügt neue Clients hinzu, die in einer Goroutine Messages lesen und schreiben können
func (m *Managment) serveWS(w http.ResponseWriter, r *http.Request) {

	log.Println("New connection")
	conn, err := websocketUpgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err)
		return
	}

	client := NewClient(conn, m)
	m.addClient(client)

	go client.readMessages()
	go client.writeMessages()
}

// fügt clients zur Clientlist hinzu
func (m *Managment) addClient(client *Client) {
	m.Lock()
	defer m.Unlock()
	m.clients[client] = true
}

// entfernt Clients von der Clientlist
func (m *Managment) removeClient(client *Client) {
	m.Lock()
	defer m.Unlock()
	if _, ok := m.clients[client]; ok {
		client.connection.Close()
		delete(m.clients, client)
	}
}
