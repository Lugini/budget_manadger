from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            print('logged in')
            return test(request, {'username': username, 'password': password})
        else:
            print('unlogged in')
            return HttpResponse("Invalid login. Please try again.")
    return render(request, 'budget/login.html', {})

def test(request, dict):
    return render(request, 'budget/test.html', dict)