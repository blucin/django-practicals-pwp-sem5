from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .form import FormDataForm
from .models import FormData

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = FormDataForm()
    return render(request, 'form.html', {'form': form})

def formData(request):
    if request.method == 'POST':
        form = FormDataForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            FormData.objects.create(username=username, email=email)
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = FormDataForm()
    return render(request, 'formData.html', {'formdata': FormData.objects.all()})