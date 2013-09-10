from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import login as django_login
from forms import LoginForm

def login(request):
    if request.user.is_authenticated():
        return redirect(reverse('comp_home'))
    return django_login(request, template_name='login.html', authentication_form=LoginForm)
