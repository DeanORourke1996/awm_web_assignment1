from django.contrib.auth.forms import UserCreationForm
from .forms import User
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = User