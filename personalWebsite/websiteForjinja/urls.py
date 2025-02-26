
from django.urls import path
from . import views 
urlpatterns = [
    
    path('', views.Education,name='Education'),
    path('incident/', views.incidentReturn,name='incident'),
    path('<int:incident_id>/', views.incidentDetail,name='incidentDetail'),
]