"""
URL configuration for drivers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView

from lauda.views.error_view import error_view
# from lauda.forms import UserForm
from lauda.views.auth_views import register_user, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',
         register_user,
         name='django_registration_register'),
    path('login/',
         login,
         name='login'),
    path('', include('lauda.urls')),
    path('', include('django_registration.backends.one_step.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
    path('404/', error_view, name="404")
]
