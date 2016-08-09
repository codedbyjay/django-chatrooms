from rest_framework import serializers

from chatrooms.models import ChatRoom, ChatMessage

class ChatRoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatRoom
        fields = ("name", "description", "private", "created", "user")

class ChatMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChatMessage
        fields = ("message", "created", "room", "user")

    def to_representation(self, obj):
        result = super(ChatMessageSerializer, self).to_representation(obj)
        result["username"] = obj.user.username
        return result

