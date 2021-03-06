from channels.routing import route
from pconsumer.consumers import  ws_disconnect, ws_add, ws_message, ws_add_id, ws_message_id, ws_disconnect_id

channel_one = [
 route('websocket.connect', ws_add),
 route('websocket.receive', ws_message),
 route('websocket.disconnect', ws_disconnect),
]

channel_two = [
    route("websocket.connect", ws_add_id),
    route("websocket.receive", ws_message_id),
    route("websocket.disconnect", ws_disconnect_id),
]