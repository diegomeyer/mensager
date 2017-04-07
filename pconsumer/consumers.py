import json
from django.http import HttpResponse
from channels import Group
from channels.handler import AsgiHandler
from channels.sessions import channel_session
from pconsumer.models import Room
from channels.auth import channel_session_user, channel_session_user_from_http
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@channel_session_user_from_http
def ws_add(message):
    print('group')
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Add them to the right group
    message.channel_session['chats'] = []
    Group("chat", channel_layer=message.channel_layer).add(message.reply_channel)
    message.channel_session['chats'] = list(set(message.channel_session['chat']).union([1]))
 
 
@channel_session_user
def ws_message(message):
    Group("chat", channel_layer=message.channel_layer).send({
        "text": message['text'],
    })
 
@channel_session_user_from_http
def ws_add_id(message):
    print('group1')
    # Accept connection
    message.reply_channel.send({"accept": True})
    # Add them to the right group
    Group("chat1", channel_layer=message.channel_layer).add(message.reply_channel)
 
@channel_session_user 
def ws_message_id(message):
    print('menssagem1')
    Group("chat1", channel_layer=message.channel_layer).send({
        "text": message['text'],
    })
 
# Connected to websocket.disconnect
@channel_session_user 
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
 
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