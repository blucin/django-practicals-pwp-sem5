from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def formData(request):
    context = {
        'username': request.POST['username'],
        'email': request.POST['email']
    }
    return render(request, 'formData.html', context)

def form(request):
    if request.method == 'POST':
        return formData(request)
    else:
        return render(request, 'form.html')