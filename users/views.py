from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def profile_update(request):
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Updated for {request.user.username}!")
            return redirect('course-home')
        else:
            messages.warning(request, f"Oops!! Please refill form correctly")
    else:
        form = ProfileUpdateForm()
    return render(request, 'users/profile_update.html', {'form': form})


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You can now login.")
            return redirect('login')
        else:
            messages.warning(request, f"Oops!! Please refill form correctly")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
