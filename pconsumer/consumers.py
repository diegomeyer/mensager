from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http
from channels.sessions import http_session

from .models import Room
import json


@http_session
@channel_session_user_from_http
def ws_add(message):
    if message.user.is_authenticated():
        room = Room.objects.get(label=0)
        message.reply_channel.send({"accept": True})        # libera o envio de mensagens
        Group("chat", channel_layer=message.channel_layer).add(message.reply_channel)
        message.channel_session['room'] = room.label

@http_session
@channel_session_user_from_http
def ws_add_id(message):
    if message.user.is_authenticated():
        # Accept connection
        room = Room.objects.get(label=1)
        message.reply_channel.send({"accept": True})        # libera o envio de mensagens
        # Add them to the right group
        Group("chat1", channel_layer=message.channel_layer).add(message.reply_channel)
        message.channel_session['room'] = room.label


@http_session
@channel_session_user
def ws_message(message):
    if message.user.is_authenticated():
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        dict_message = json.loads(message['text'])
        m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
        Group("chat", channel_layer=message.channel_layer).send({
              "text": json.dumps(m.as_dict()),
        }),
    else:
        message.reply_channel.send({
            "text": json.dumps({"error": u"O usuário não está logado."}),
        })


@http_session
@channel_session_user
def ws_message_id(message):
    if message.user.is_authenticated():
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        dict_message = json.loads(message['text'])
        m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
        Group("chat1", channel_layer=message.channel_layer).send({
              "text": json.dumps(m.as_dict()),
        }),
    else:
        message.reply_channel.send({
            "text": json.dumps({"error": u"O usuário não está logado."}),
        })

# Connected to websocket.disconnect
@http_session
@channel_session_user
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


@http_session
@channel_session_user
def ws_disconnect_id(message):
    Group("chat1").discard(message.reply_channel)