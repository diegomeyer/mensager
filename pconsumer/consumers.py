from channels import Group
from channels.sessions import channel_session
from channels.auth import channel_session_user, channel_session_user_from_http
from .models import Message, Room
import json


@channel_session_user_from_http
def ws_add(message):
    room = Room.objects.get(label=0)
    message.reply_channel.send({"accept": True})        # libera o envio de mensagens
    Group("chat", channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = room.label


@channel_session_user_from_http
def ws_add_id(message):
    # Accept connection
    room = Room.objects.get(label=1)
    message.reply_channel.send({"accept": True})        # libera o envio de mensagens
    # Add them to the right group
    Group("chat1", channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = room.label


@channel_session_user
def ws_message(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    dict_message = json.loads(message['text'])
    m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
    Group("chat", channel_layer=message.channel_layer).send({
        "text": json.dumps(m.as_dict()),
    })


@channel_session_user
def ws_message_id(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    dict_message = json.loads(message['text'])
    m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
    Group("chat1", channel_layer=message.channel_layer).send({
        "text": json.dumps(m.as_dict()),
    })


# Connected to websocket.disconnect
@channel_session_user
def ws_disconnect(message):
    Group("chat-%s" % message.user.username[0]).discard(message.reply_channel)


@channel_session_user
def ws_disconnect_id(message):
    Group("chat1-%s" % message.user.username[0]).discard(message.reply_channel)