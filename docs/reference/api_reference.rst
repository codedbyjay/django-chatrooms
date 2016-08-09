=============
API Reference
=============


Channels
========

We use several channels that users will subscribe to for messages of a certain nature.

- **Room Channel** every room has a Channel with the name ``room-<room_id>``. This room receives the following messages:
    - New messages using the ID of "chat-message"
    - Participant joining the room. These messages use an ID of "participant-join".
    - Participant leaving the room. These messages use an ID of "participant-leave".

- **System Channel** this room is used for system messages such as:
    - New chat rooms - users are notified of new public chatrooms that are created here. These message are sent with a request_type of "chatroom". 

PUSH Messages
====================

Several messages are sent from the server to the client.

- **Invitations** - invitations to chatrooms are sent directly to client sockets.


Models
======

ChatRoom
--------

..  autoclass:: chatrooms.models.ChatRoom

    ..  attribute:: name 

        The name of the chat room

    ..  attribute:: description

        The description of the chat room

    ..  attribute:: private

        Indicates whether the room is private or not. Users must be explicitly invited to join private rooms.

    ..  attribute:: users

        The users that are allowed to enter this room. This list is typically empty is the room is not ``private``.

    ..  attribute:: participants

        The users that are currently in the room.

    ..  attribute:: team

        The team that owns the chatroom, this is None if this is not a team chat.

    ..  attribute:: user

        The user that created the ``ChatRoom``.



ChatMessage
-----------

..  autoclass:: chatrooms.models.ChatMessage

    ..  attribute:: message

        The text version of the message

    ..  attribute:: room

        The ``room`` that the message was sent in.

    ..  attribute:: user

        The ``user`` that sent the message.


Team
----

..  autoclass:: chatrooms.models.ChatMessage

    ..  attribute:: message

        The text version of the message

    ..  attribute:: room

        The ``room`` that the message was sent in.

