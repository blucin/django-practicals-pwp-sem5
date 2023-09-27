from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def demo(request):
    context = {
        'variable': 'This is a variable',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'demo.html', context)
