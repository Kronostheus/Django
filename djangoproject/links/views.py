from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Link, Vote

# Create your views here.
def index(request):
    links = Link.objects.all()[:10]

    context = {
        'links': links
    }

    return render(request, 'links/index.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})