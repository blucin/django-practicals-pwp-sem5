from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import uploadFileForm
from prac9_4.models import fileFormSchema

# Create your views here.
def index(request):
    return render(request, 'index.html')

def fileForm(request):
    if request.method == 'POST':
        form = uploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fileName = form.cleaned_data['fileName']
            file = form.cleaned_data['file']
            # write file to MEDIA_ROOT in chunks to prevent memory issues
            with open(settings.MEDIA_ROOT + fileName, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # save file details to database
            form.save()
            return HttpResponseRedirect('/prac9_4/fileFormData/')
    else:
        form = uploadFileForm()
    return render(request, 'fileForm.html', {'form': form})

def fileFormData(request):
    files = fileFormSchema.objects.all()
    return render(request, 'fileFormData.html', {'files': files})