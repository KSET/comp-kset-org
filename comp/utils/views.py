from django.shortcuts import redirect
from django.contrib.auth.views import login as django_login
from forms import LoginForm

def login(request, *args, **kwargs):
    if request.user.is_authenticated():
        return redirect('/')
    kwargs['template_name'] = 'login.html'
    kwargs['authentication_form'] = LoginForm
    return django_login(request, *args, **kwargs)
