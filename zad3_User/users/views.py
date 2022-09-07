from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset_form.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = 'login'


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Dear {username}, you have been successfully signed up!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    username = request.user.username
    date_register = request.user.date_joined.strftime('%m/%d/%Y')
    failed_login = request.user.profile.last_login_failed.strftime('%m/%d/%Y %H:%M:%S')
    messages.info(request, f"Hi {username}! You've been with us since: {date_register}")
    messages.warning(request, f"Last failed login: {failed_login}")
    return render(request, 'users/profile.html')
