from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings

def index (request):
    return redirect(settings.HOME_REDIRECT_URL)

def about(request):
	return render(request, 'core/about.html')


