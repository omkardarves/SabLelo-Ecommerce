from django.shortcuts import render
from django.http import HttpResponse
from modules import test

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def test_logic(request):
    return HttpResponse(test.logic())