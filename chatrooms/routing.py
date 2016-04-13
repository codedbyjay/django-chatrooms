from channels.routing import route

channel_routing = [
    route("websocket.connect", "chatrooms.consumers.ws_connect"),
    route("websocket.receive", "chatrooms.consumers.ws_receive"),
    route("websocket.disconnect", "chatrooms.consumers.ws_disconnect"),
]
