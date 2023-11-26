
defmodule CounterWeb.CounterLive do
    use CounterWeb, :live_view

    @topic "counter_increase"

    def mount(params, session, socket) do
        CounterWeb.Endpoint.subscribe(@topic)
        {:ok, assign(socket, :counter_value, 0)}
    end
    def render(assigns) do
        ~H"""
            <h1>Live Counter</h1>
            <div id="counter">
                Counter value: <%= @counter_value %>
            </div>
            <button phx-click="add-1"> +1 </button>
            <button phx-click="add-5"> +5 </button>
            <button phx-click="add-10"> +10 </button>
        """
    end
    def handle_event("add-1", _, socket) do
        counter_value= socket.assigns.counter_value + 1
        CounterWeb.Endpoint.broadcast_from(self(), @topic,
        "counter_increase_event",
        counter_value)
        {:noreply, assign(socket, :counter_value, counter_value)}
    end
    def handle_event("add-5", _, socket) do
        counter_value= socket.assigns.counter_value + 5
        CounterWeb.Endpoint.broadcast_from(self(), @topic,
        "counter_increase_event",
        counter_value)
        {:noreply, assign(socket, :counter_value, counter_value)}
    end
    def handle_event("add-10", _, socket) do
        counter_value= socket.assigns.counter_value + 10
        CounterWeb.Endpoint.broadcast_from(self(), @topic,
        "counter_increase_event",
        counter_value)
        {:noreply, assign(socket, :counter_value, counter_value)}
    end
    def handle_info( %{topic: @topic, payload: new_counter_value}, socket ) do
        {:noreply, assign(socket, :counter_value, new_counter_value)}
    end
end
