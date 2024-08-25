from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.shortcuts import redirect
from django.contrib.auth import logout

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def logout_view(request):
    logout(request)
    return redirect('home')  # Logoutdan keyin qaysi sahifaga o'tish kerakligini aniqlang
