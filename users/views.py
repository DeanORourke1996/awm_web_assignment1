from .forms import UserRegisterForm
from .forms import UserLoginForm
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account was created. Please log in')
            return redirect('login')
        else:
            form = UserRegisterForm()
        return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Signed in successfully, Welcome')
            return redirect('home')
        else:
            return redirect('login/error')
        return render(request, 'accounts/')