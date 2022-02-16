from django.shortcuts import  render, redirect
from .forms import NewCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

def register(request):
	if request.method == "POST":
		form = NewCreationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("logreg:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewCreationForm()
	return render (request, "register.html", {"form":form})

def mylogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('logreg:index')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def mylogout(request):
    logout(request)
    return redirect('logreg:index')
    
def index(request):
    return render(request, 'index.html')