from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from chatrooms.views import LoginView, RegisterView, HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
]
