from django.shortcuts import render
from .models import TellTheStroy
from django.shortcuts import get_object_or_404
from .forms import IncidentForm
# Create your views here.
# def Incident(request):
#     incident=None
#     if request.method == 'POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         memoryTitle=request.POST.get('memoryTitle')
#         dateOfMemory=request.POST.get('dateOfMemory')
#         story=request.POST.get('story')
#         image=request.POST.get('image')
#         date_posted=request.POST.get('date_posted')
#         incident=TellTheStroy(name=name,email=email,memoryTitle=memoryTitle,dateOfMemory=dateOfMemory,story=story,image=image,date_posted=date_posted)
#         incident.save()
#     return render(request, 'incident.html')

def Incident(request):
    incident=None
    if request.method == 'POST':
        form=IncidentForm(request.POST)
        if form.is_valid():
            incident=TellTheStroy(name=form.cleaned_data['name'],email=form.cleaned_data['email'],memoryTitle=form.cleaned_data['memoryTitle'],dateOfMemory=form.cleaned_data['dateOfMemory'],story=form.cleaned_data['story'],image=form.cleaned_data['image'],date_posted=form.cleaned_data['date_posted'])
            incident.save() 
    return render(request, 'incident.html')

def incidentReturn(request):
    StoryData=TellTheStroy.objects.all()
    return render(request, 'PageToSeeincident.html',{'Alldata':StoryData})

def incidentDetail(request,incident_id):
    aboutIncident=get_object_or_404(TellTheStroy,pk=incident_id)
    return render(request, 'incidentDetail.html',{'incident':aboutIncident}) 

def testForm(request):
    incident=None
    if request.method == 'POST':
        form=IncidentForm(request.POST)
        if form.is_valid():
            incident=TellTheStroy(name=form.cleaned_data['name'],email=form.cleaned_data['email'],memoryTitle=form.cleaned_data['memoryTitle'],dateOfMemory=form.cleaned_data['dateOfMemory'],story=form.cleaned_data['story'],image=form.cleaned_data['image'],date_posted=form.cleaned_data['date_posted'])
            incident.save() 
    else:
        form=IncidentForm()
    return render(request, 'testform.html', {'form':form})