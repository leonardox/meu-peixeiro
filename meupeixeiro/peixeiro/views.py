from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from peixeiro.models import UserPeixeiro


@login_required(login_url='/login')
def index(request):
    """
    Index page.
    """
    return render_to_response('index.html', context_instance=RequestContext(request))


def do_login(request):
    """
    The login page.
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render_to_response('index.html', context_instance=RequestContext(request))
            else:
                return render_to_response('login.html', context_instance=RequestContext(request))
        else:
            return render_to_response('login.html', context_instance=RequestContext(request))

    else:
        return render_to_response('login.html', context_instance=RequestContext(request))


def do_logout(request):
    """
    Logout an user.
    """
    logout(request)
    return render_to_response('login.html', context_instance=RequestContext(request))


def add_user(request):
    """
    View to add a new user.
    """
    if request.method == "POST":
        data = request.POST
        UserPeixeiro.create(data)
        return index(request)
    else:
        return render_to_response('addUser.html', context_instance=RequestContext(request))
