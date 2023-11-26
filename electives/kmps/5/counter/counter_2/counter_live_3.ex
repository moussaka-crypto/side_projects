
defmodule CounterWeb.CounterLive do
    use CounterWeb, :live_view

    def mount(params, session, socket) do
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
        {:noreply, assign(socket, :counter_value, counter_value)}
    end
    def handle_event("add-5", _, socket) do
        counter_value= socket.assigns.counter_value + 5
        {:noreply, assign(socket, :counter_value, counter_value)}
    end
    def handle_event("add-10", _, socket) do
        counter_value= socket.assigns.counter_value + 10
        {:noreply, assign(socket, :counter_value, counter_value)}
    end
end
