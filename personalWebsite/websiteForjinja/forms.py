from django import forms
from .models import TellTheStroy
from django.utils import timezone
class IncidentForm(forms.Form):
    name=forms.ModelChoiceField(queryset=TellTheStroy.objects.all(), label='Name')
    email=forms.EmailField(max_length=100, label='Email')
    memoryTitle=forms.CharField(max_length=100, label='Memory Title')
    dateOfMemory=forms.DateField(label='Date of Memory')
    story= forms.CharField(max_length=1000 ,label='Story')
    image = forms.ImageField(label='Image')
    date_posted = forms.DateTimeField(label='Date Posted')

class testingForm(forms.Form):
    name=forms.CharField(max_length=100, label='Name')
    email=forms.EmailField(max_length=100, label='Email')
    memoryTitle=forms.CharField(max_length=100, label='Memory Title')
    dateOfMemory=forms.DateField(label='Date of Memory')
    story= forms.CharField(max_length=1000 ,label='Story')
    image = forms.ImageField(label='Image')
    date_posted = forms.DateTimeField(label='Date Posted')
