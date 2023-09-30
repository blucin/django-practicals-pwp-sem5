from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import simpleForm
from prac9_3.models import FormSchema

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = simpleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = simpleForm()
    return render(request, 'form.html', {'form': form})

def formData(request):
    if request.method == 'POST':
        form = simpleForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            FormSchema.objects.create(username=username, email=email)
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = simpleForm()
    return render(request, 'formData.html', {'formdata': FormSchema.objects.all()})