from __future__ import unicode_literals

from django.db import models
from django.conf import settings

from django_extensions.db.models import TimeStampedModel
from autoslug import AutoSlugField


class ChatRoom(TimeStampedModel):

    name = models.CharField("Chat Room", max_length=255)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(blank=True, null=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="rooms")
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="active_rooms")
    team = models.ForeignKey(
        "Team", blank=True, null=True, related_name="rooms")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="created_rooms")
    private = models.BooleanField(default=False)

class ChatMessage(TimeStampedModel):

    message = models.TextField(blank=True, null=True)
    room = models.ForeignKey("ChatRoom", related_name="messages")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="messages")


class Team(TimeStampedModel):

    name = models.CharField("Team", max_length=255)
    slug = AutoSlugField(populate_from='name')
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="teams")

