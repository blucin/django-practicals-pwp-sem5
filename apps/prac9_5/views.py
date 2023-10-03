from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import createAccountForm, loginForm
from prac9_5.models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def createAccount(request):
    if request.method == 'POST':
        form = createAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/prac9_5/login/')
    else:
        form = createAccountForm()
    return render(request, 'createAccount.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username, password=password)
                return HttpResponseRedirect('/prac9_5/loginSuccess/')
            except User.DoesNotExist:
                return HttpResponseRedirect('/prac9_5/loginFail/')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def loginSuccess(request):
    return render(request, 'loginSuccess.html')

def loginFail(request):
    return render(request, 'loginFail.html')