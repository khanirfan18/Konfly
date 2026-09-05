from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignUpForm
# Create your views here.

class HandleOldUser(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class HandleNewUser(CreateView):
    form_class = SignUpForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy("home")

    redirect_authenticated_user = True


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect("home")


