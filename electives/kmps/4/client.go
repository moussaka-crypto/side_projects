package main

import (
	"github.com/gorilla/websocket"
	"log"
)

// Map mit allen Clients
type ClientList map[*Client]bool

// Websocket Client bzw. Besucher des Frontends
type Client struct {
	connection         *websocket.Conn
	manager            *Managment
	unbuffered_channel chan []byte
}

// Neuer Client
func NewClient(conn *websocket.Conn, manager *Managment) *Client {
	return &Client{
		connection:         conn,
		manager:            manager,
		unbuffered_channel: make(chan []byte),
	}
}

// liest Nachrichten und broadcastet sie zu allen Clients
func (c *Client) readMessages() {
	defer func() {
		c.manager.removeClient(c)
	}()

	for {
		messageType, payload, err := c.connection.ReadMessage()

		if err != nil {
			if websocket.IsUnexpectedCloseError(err, websocket.CloseGoingAway, websocket.CloseAbnormalClosure) {
				log.Printf("error reading message: %v", err)
			}
			break
		}
		log.Println("Daten auf Server:", string(payload))
		log.Println("Server erkennt message type:", messageType)

		for wsclient := range c.manager.clients {
			wsclient.unbuffered_channel <- payload
		}
	}
}

//wartet auf neue messages, die zum Client gesendet werden können
func (c *Client) writeMessages() {
	defer func() {

		c.manager.removeClient(c)
	}()

	for {
		select {
		case message, ok := <-c.unbuffered_channel:
			if !ok {
				if err := c.connection.WriteMessage(websocket.CloseMessage, nil); err != nil {
					log.Println("connection closed: ", err)
				}
				return
			}
			if err := c.connection.WriteMessage(websocket.TextMessage, message); err != nil {
				log.Println(err)
			}
		}
	}
}
