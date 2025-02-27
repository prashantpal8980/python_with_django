
from django.urls import path
from . import views 
urlpatterns = [
    
    path('', views.Incident,name='incident'),
    path('incident/', views.incidentReturn,name='PageToSeeincident'),
    path('<int:incident_id>/', views.incidentDetail,name='incidentDetail'),
    path('test/', views.testForm,name='test'),
]