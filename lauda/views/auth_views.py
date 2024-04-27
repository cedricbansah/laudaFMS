from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect
from django.urls import reverse

from lauda.forms.login_form import LoginForm
from django.contrib.auth.models import User
from lauda.serializers.auth_serializers.login_serializer import LoginSerializer
from lauda.serializers.auth_serializers.register_serializer import RegisterSerializer


def register_user(request):
    if request.method == "POST":

        register_serializer = UserCreationForm(data=request.POST)

        if register_serializer.is_valid():
            register_serializer.save()

            return redirect(reverse("login"))
        print(register_serializer.errors)
        return redirect(reverse("404"))
    form = UserCreationForm()
    return render(request, "django_registration/registration_form.html", {'form': form})


def login(request):

    if request.method == "POST":
        login_serializer = LoginForm(data=request.POST)
        if login_serializer.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            try:
                user = User.objects.get(username = username)
            except User.DoesNotExist:
                return redirect(reverse("404"))
            if user.check_password(password):
                request.session['user_id'] = user.id
                return redirect(reverse("index"))
            return redirect(reverse("404"))
    form = LoginForm()
    return render(request, "django_registration/login_form.html", {'form': form})

