from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from users.forms import UserRegistrationForm
from users.models import User


@login_required
def profile(request):
    return render(request,
                  'users/profile.html')


class SingUpView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy("accounts:login")
    success_message = 'Account created for %(username)s'
    template_name = "users/signup.html"

    class Meta:
        model = User
        fields = (
            'username',
            'avatar',
        )


class UserUpdateView(UpdateView):
    model = User
    fields = (
        "username",
        "avatar",
    )
    template_name = "users/profile_edit.html"
    success_url = reverse_lazy('accounts:profile')
