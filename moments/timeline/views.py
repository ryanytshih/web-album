import logging as log

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import PhotoModelForm
from .models import Photo

# Create your views here.


@login_required(login_url="login")
def index(request):
    photos = Photo.objects.order_by("-time")

    return render(request, "timeline/index.html", locals())

@login_required(login_url="login")
def upload(request):
    form = PhotoModelForm()

    context = {
        "form": form
    }

    if request.method == "POST":
        log.info("POST")
        form = PhotoModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/timeline")
        else:
            log.info(str(form.errors))
            log.info(str(request.POST))
            from datetime import datetime

            # time = datetime.strptime(request.POST.get("time"), "%Y-%m-%d %I:%M %p")
            # log.info(str(time))
            log.info("form invalid")
    
    return render(request, "timeline/upload.html", context)

@login_required(login_url="login")
def update(request, pk):
    photo = Photo.objects.get(id=pk)
    form = PhotoModelForm(instance=photo)

    context = {
        "form": form,
        "photo": photo
    }

    if request.method == "POST":
        form = PhotoModelForm(request.POST, request.FILES, instance=photo)
        
        if form.is_valid():
            form.save()
            return redirect("/timeline")
        else:
            log.info(str(form.non_field_errors))
            log.info(str(form.errors))
            log.info(str(request.POST))
            from datetime import datetime

            # time = datetime.strptime(request.POST.get("time"), "%Y-%m-%d %I:%M %p")
            # log.info(str(time))
            log.info("form invalid")
    
    return render(request, "timeline/update.html", context)

@login_required(login_url="login")
def delete(request, pk):
    photo = Photo.objects.get(id=pk)
    
    context = {
        "photo": photo
    }

    if request.method == "POST":
        photo.delete()
        return redirect("/timeline")

    return render(request, "timeline/delete.html", context)
