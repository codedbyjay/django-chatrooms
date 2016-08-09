from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter

from chatrooms.views import *

router = DefaultRouter()
router.register(r'room', ChatRoomViewSet)
router.register('message', ChatMessageViewSet)

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^docs/', include('docs.urls')),

    # DRF API
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
