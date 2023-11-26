defmodule ChatWeb.ChatLive do
  use ChatWeb, :live_view
  
  @topic "chat_increase"
  
  def mount(_params, _session, socket) do
    if connected?(socket) do
      ChatWeb.Endpoint.subscribe(@topic)
      end
      {:ok, assign(socket, messages: [], username: nil)}
  end 
  def render(assigns) do
    ~H"""
    <div>
      <h1>Live Chat</h1>
      <div class="messages" style="border: 1px solid #eee; height: 400px; overflow: scroll; margin-bottom: 8px;">
        <%= for m <- @messages do %>
          <p style="margin: 2px;"><b><%= m.name %></b>: <%= m.text %></p>
        <% end %>
      </div>
      <%= if !@username do %>
        <form phx-submit="set_username">
          <input type="text" name="username" placeholder="Geben Sie bitte ihren Usernamen ein." />
          <button type="submit">Bestätigen</button>
        </form>
      <% end %>
      <form phx-submit="send">
        <input type="text" name="text" placeholder="Geben Sie bitte ihre Nachricht ein." />
        <button type="submit">SEND</button>
      </form>
    </div>
    """
  end
  def handle_event("send", %{"text" => text}, socket) do
    username = socket.assigns.username
    ChatWeb.Endpoint.broadcast(@topic, "message", %{text: text, name: username})
    {:noreply, socket}
  end
  def handle_event("set_username", %{"username" => username}, socket) do
    {:noreply, assign(socket, username: username)}
  end
  def handle_info(%{event: "message", payload: message}, socket) do
    {:noreply, assign(socket, messages: socket.assigns.messages ++ [message])}
  end
end
 
