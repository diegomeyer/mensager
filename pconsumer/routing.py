from channels.routing import route
from pconsumer.consumers import ws_connect, ws_message, ws_disconnect, ws_add

channel_routing = [
    route("websocket.connect", ws_add), 
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
]