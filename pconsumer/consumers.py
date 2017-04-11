# -*- coding: utf-8 -*-

from channels import Group
from channels.auth import channel_session_user, channel_session_user_from_http

from .models import Room, Connection
import json

@channel_session_user_from_http
def ws_add(message):
    user = message.user
    if user.is_authenticated():
        room = Room.objects.get(label=0)
        Connection.objects.get_or_create(room=room, user=user)
        message.channel_session['room'] = room.label
        print(str(user) + ' entrou na sala.')
        message.reply_channel.send({"accept": True})                       # libera o envio de mensagens
        Group('chat', channel_layer=message.channel_layer).add(message.reply_channel)


@channel_session_user_from_http
def ws_add_id(message):
    user = message.user
    if user.is_authenticated():
        # Accept connection
        room = Room.objects.get(label=1)
        message.reply_channel.send({"accept": True})        # libera o envio de mensagens
        # Add them to the right group
        Group("chat1", channel_layer=message.channel_layer).add(message.reply_channel)
        message.channel_session['room'] = room.label


@channel_session_user
def ws_message(message):
    user = message.user
    if user.is_authenticated():
        label = message.channel_session['room']
        room = Room.objects.get(label=label)
        if Connection.objects.filter(room=room, user=user).count() != 0:
            dict_message = json.loads(message['text'])
            m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
            Group('chat', channel_layer=message.channel_layer).send({
                  "text": json.dumps(m.as_dict()),
            }),
        else:
            message.reply_channel.send({
                "text": json.dumps({"error": u"O usuário não está logado."}),
            })


@channel_session_user
def ws_message_id(message):
    user = message.user
    if user.is_authenticated():
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


@channel_session_user
def ws_disconnect(message):
    user = message.user
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    connections = Connection.objects.filter(room=room, user=user)
    if connections.count() != 0:
        connections.get(room=room, user=user).delete()
        Group("chat").discard(message.reply_channel)
        print('Usuario '+ str(user) + ' desconectado.')


@channel_session_user
def ws_disconnect_id(message):
    Group("chat1").discard(message.reply_channel)