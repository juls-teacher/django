import logging
from django.http import HttpResponse
from profiles.forms import RegisterForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from profiles.models import Profile

logger = logging.getLogger(__name__)

def profiles(request):
    if request.GET.get("param"):
        logger.info(f' My param = {request.GET.get("param")}')
    return HttpResponse("profiles view")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(username=form.cleaned_data["username"],
                                       email=form.cleaned_data["email"],
                                       password=form.cleaned_data["password"],)
            Profile.objects.create(user_id=user.id,
                                   first_name=form.cleaned_data["first_name"],
                                   last_name=form.cleaned_data["last_name"],
                                   age=form.cleaned_data["age"])

            logger.info(f"user email: {form.cleaned_data['email']}")
            logger.info(f"user password: {form.cleaned_data['password']}")
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})

