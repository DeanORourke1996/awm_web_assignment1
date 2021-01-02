from django.contrib import admin
from django.contrib.auth import views as auth
from users import views as users
from locations import views as locations
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', locations.home, name='home'),
    path('locations/', locations.countries, name='locations'),
    path('home/', locations.home, name='home'),
    path('login/', auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', users.register, name='register')
]
