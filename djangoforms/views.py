from django.shortcuts import render
from django.http import HttpResponse
from djangoforms.forms import Wanafunzi
from djangoforms.functions import handle_uploaded_files


def index(request):
    if request.method == 'POST':
        student = Wanafunzi(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_files(request.FILES)
            return HttpResponse("Uploaded successfully")
    else:
        student = Wanafunzi()
        return render(request, 'index.html', {'form': student})
