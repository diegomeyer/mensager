<<<<<<< HEAD
=======
import json
from django.http import HttpResponse
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3
from channels import Group
from channels.sessions import channel_session
from pconsumer.models import Room
from channels.auth import channel_session_user, channel_session_user_from_http
<<<<<<< HEAD
from .models import Message, Room
import json

=======
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3

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
<<<<<<< HEAD
    Group("chat1", channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['room'] = room.label


@channel_session_user
def ws_message(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    dict_message = json.loads(message['text'])
    m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
=======
    message.channel_session['chats'] = []
    Group("chat", channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['chats'] = list(set(message.channel_session['chat']).union([1]))
 
 
@channel_session_user
def ws_message(message):
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3
    Group("chat", channel_layer=message.channel_layer).send({
        "text": json.dumps(m.as_dict()),
    })
<<<<<<< HEAD


@channel_session_user
=======
 
@channel_session_user_from_http
def ws_add_id(message):
    print('group1')
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Add them to the right group
    Group("chat1", channel_layer=message.channel_layer).add(message.reply_channel)
 
@channel_session_user 
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3
def ws_message_id(message):
    label = message.channel_session['room']
    room = Room.objects.get(label=label)
    dict_message = json.loads(message['text'])
    m = room.messages.create(handle=dict_message['user'], message=dict_message['message'])
    Group("chat1", channel_layer=message.channel_layer).send({
        "text": json.dumps(m.as_dict()),
    })
<<<<<<< HEAD


=======
 
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3
# Connected to websocket.disconnect
@channel_session_user 
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
<<<<<<< HEAD


@channel_session_user
def ws_disconnect_id(message):
    Group("chat1").discard(message.reply_channel)
=======
 
@channel_session_user
def ws_disconnect_id(message):
    Group("chat1").discard(message.reply_channel)
     
     
@channel_session
def ws_connect(message):
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Work out room name from path (ignore slashes)
    room = message.content['path'].strip("/")
    # Save room in session and add us to the group
    message.channel_session['room'] = room
    Group("chat-%s" % room).add(message.reply_channel)    
>>>>>>> b537af9f20abdbe302c6a96c8a5246d4a30ed4a3
