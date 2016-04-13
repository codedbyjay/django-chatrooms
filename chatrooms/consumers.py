import json

from django.contrib import auth
from channels import Group
from channels.auth import channel_session_user_from_http, channel_session_user
from channels.sessions import channel_session


@channel_session_user_from_http
def ws_connect(message):
    from channels.sessions import session_for_reply_channel
    user = message.user
    Group("online").add(message.reply_channel)
    Group("chat").add(message.reply_channel)


@channel_session_user
def ws_receive(message):
    user = message.user
    text = message.content['text']
    print("%s sent message: %s" % (message.user, text))
    username = message.user.username
    Group("chat").send({
        "text": json.dumps(dict(text=text, user=username))
    })


@channel_session_user
def ws_disconnect(message):
    from channels.sessions import session_for_reply_channel
    user = message.user
    print("%s went offline" % user)
    Group("online").discard(message.reply_channel)
    Group("chat").discard(message.reply_channel)
