from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
        return render(request, 'SOYIN/index.html', {})
def index2(request):
        return render(request, 'SOYIN/index2.html', {})
