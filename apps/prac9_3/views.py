from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import simpleForm
from .models import formSchema

# Create your views here.
def index(request):
    return render(request, 'index.html')

def form(request):
    if request.method == 'POST':
        form = simpleForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            formSchema.objects.create(username=username, email=email)
            return HttpResponseRedirect('/prac9_3/formData/')
    else:
        form = simpleForm()
    return render(request, 'form.html', {'form': form})

def formData(request):
    formdata = formSchema.objects.all()
    return render(request, 'formData.html', {'formdata': formdata})