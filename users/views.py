from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from . import forms,models


class NewLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "login.html"
    success_url = "/users/"


class RegisterView(CreateView):
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url = "/users/"

class UserListView(ListView):
    queryset = models.CustomUser.objects.all()
    template_name = "user_list.html"

    def get_queryset(self):
        return self.queryset
