from .forms import UserRegisterForm
from django.shortcuts import render, redirect


# Create your views here.
def register(response):
    form = UserRegisterForm(response.POST)
    if response.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("/home")
        else:
            form = UserRegisterForm()

    return render(response, "users/register.html", {"form": form})