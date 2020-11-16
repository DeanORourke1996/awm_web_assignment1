from django.urls import path
from .views import UserRegisterForm


urlpatterns = [
    path('register/', UserRegisterForm.as_view(), name='signup'),
]
