from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm


def landing_page(request):
    return render(request, "landing/index.html")


def user_list(request):
    users = Profile.objects.all()
    return render(request, "landing/user_list.html", {"users": users})


def create_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.client_category = "Bronze"
            profile.save()
            return redirect("user_list")
    else:
        form = ProfileForm()
    return render(request, "landing/create_profile.html", {"form": form})
