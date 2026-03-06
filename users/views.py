from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import HumanCreationForm, CustomAuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = HumanCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a page after successful signup
    else:
        form = HumanCreationForm()

    return render(request, 'user/signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a page after successful login
    else:
        form = CustomAuthenticationForm()

    return render(request, 'user/login.html', {'form': form})


def logout_func(request):
    logout(request)
    return redirect("/")