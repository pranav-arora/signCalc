from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def index(request):
    context={"message": "hello"}
    return render(request, 'music/hey.html', context)
