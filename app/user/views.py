from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.conf import settings

from .forms import SignUpForm

def index(request):
	return HttpResponse("wasup")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.projects_wanted = form.cleaned_data.get('projects_wanted')
            user.profile.email_confirmed = form.cleaned_data.get('email_confirmed')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})