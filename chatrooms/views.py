from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib import messages

from registration.backends.simple.views import RegistrationView
from chatrooms.forms import LoginForm, RegistrationForm


class HomeView(LoginRequiredMixin, TemplateView):

    template_name = "chatrooms/home.html"
    login_url = '/login/'


class LoginView(FormView):

    template_name = "chatrooms/login.html"
    form_class = LoginForm

    def form_valid(self, form):
        cleaned_data = form.cleaned_data
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
            return redirect("/")
        messages.error(self.request, "Incorrect username or password")
        return self.get(self.request)


class RegisterView(RegistrationView):

    form_class = RegistrationForm
    template_name = "chatrooms/register.html"
