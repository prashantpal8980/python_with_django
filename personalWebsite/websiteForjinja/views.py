from django.shortcuts import render
from .models import TellTheStroy
# Create your views here.
def Education(request):
    # StoryData=TellTheStroy.objects.all()
    # ,{'Alldata':StoryData}
    return render(request, 'incident.html')

def incidentReturn(request):
    StoryData=TellTheStroy.objects.all()
    return render(request, 'PageToSeeincident.html',{'Alldata':StoryData})