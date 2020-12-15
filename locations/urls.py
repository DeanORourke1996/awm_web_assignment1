from django.urls import path
from . import views

urlpatterns = [
    path("<string>:name", views.index, name='index')
]
