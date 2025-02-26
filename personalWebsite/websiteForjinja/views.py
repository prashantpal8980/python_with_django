from django.shortcuts import render
from .models import TellTheStroy
from django.shortcuts import get_object_or_404
# Create your views here.
def Education(request):
    # StoryData=TellTheStroy.objects.all()
    # ,{'Alldata':StoryData}
    return render(request, 'incident.html')

def incidentReturn(request):
    StoryData=TellTheStroy.objects.all()
    return render(request, 'PageToSeeincident.html',{'Alldata':StoryData})

def incidentDetail(request,incident_id):
    aboutIncident=get_object_or_404(TellTheStroy,pk=incident_id)
    return render(request, 'incidentDetail.html',{'incident':aboutIncident}) 