
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
        """
    end
end
