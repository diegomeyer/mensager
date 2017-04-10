from channels.routing import route
<<<<<<< HEAD
from pconsumer.consumers import ws_message, ws_disconnect, ws_add, ws_message_id, ws_add_id, ws_disconnect_id
=======
from pconsumer.consumers import  ws_disconnect, ws_add, ws_message
# from pconsumer.consumers import ws_connect, ws_message, ws_disconnect, ws_add, ws_message_id, ws_add_id, ws_disconnect_id
from channels.staticfiles import StaticFilesConsumer
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3

channel_one= [
 route('http.request', StaticFilesConsumer()),
 route('websocket.connect', ws_add),
 route('websocket.receive', ws_message),
 route('websocket.disconnect', ws_disconnect),
]

# channel_two = [
#     route("websocket.connect", ws_add_id),
#     route("websocket.receive", ws_message_id),
#     route("websocket.disconnect", ws_disconnect_id),
# ]