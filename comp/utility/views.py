from django.shortcuts import redirect

def redirect_if_logged_in(view, url='/'):
    def new_view(request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(url)
        return view(request, *args, **kwargs)
    return new_view
