from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse('Hello, Prashant here')
   return render(request, 'index.html')

def about(request):
    return HttpResponse('Well i am a Cyber Security Enthusiast and love linux over windows')

def contact(request):
    return HttpResponse('You can contact me at my email or at this website')

def hobbies(request):
    return HttpResponse('I love to liten to music ')