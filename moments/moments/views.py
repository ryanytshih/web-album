import os
import random

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from django.shortcuts import redirect, render
from timeline.forms import LoginForm
from timeline.models import Photo


@login_required(login_url="login")
def index(request):
    photo_pks = Photo.objects.values_list("pk", flat=True)
    photo_num = len(photo_pks)
    random_pks = random.sample(list(photo_pks), 3)
    photos = Photo.objects.filter(pk__in=random_pks)

    context = {
        "photos": photos,
        "photo_num": photo_num
    }
    
    return render(request, "home.html", context)

def log_in(request):

    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET.get("next", "/"))

    context = {
        "form": form
    }

    return render(request, "login.html", context)

def log_out(request):

    logout(request)
    return redirect("/login")

@login_required(login_url="login")
def protected_media(request, img_path):
    img = open(os.path.join(settings.MEDIA_ROOT, "photos", img_path), 'rb')

    response = FileResponse(img)

    return response