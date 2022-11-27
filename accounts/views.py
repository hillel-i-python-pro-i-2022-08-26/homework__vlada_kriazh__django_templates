from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from .forms import LoginForm
from .forms import RegisterForm


@login_required
def profile(request):
    return render(request, 'users/profile.html')


# def profile(request: HttpRequest) -> HttpResponse:
#     return render(
#         request,
#         'registration/../templates/users/profile.html',
#         {'request': request}
#     )


# class SingUpView(CreateView):
#     form_class = UserRegistrationForm
#     # success_url = reverse_lazy("login")
#     template_name = "users/signup.html"
#
#     class Meta:
#         model = User
#         fields = (
#             'username',
#             'avatar',
#         )


class SingUpView(CreateView):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = "users/signup.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='/accounts/login/')

        return render(request, self.template_name, {'form': form})

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(SingUpView, self).dispatch(request, *args, **kwargs)


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        # remember_me = form.cleaned_data.get('remember_me')
        #
        # if not remember_me:
        #     # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
        #     self.request.session.set_expiry(0)
        #
        #     # Set session as modified to force data updates/cookie to be saved.
        #     self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)
