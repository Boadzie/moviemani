from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, LoginForm


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
