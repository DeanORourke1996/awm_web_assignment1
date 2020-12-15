from django.urls import path
from .views import UserRegisterForm


urlpatterns = [
    path('', UserRegisterForm.as_view(), name='register'),
]
