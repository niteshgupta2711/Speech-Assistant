from django.contrib import admin
from django.urls import path
from Home import views

from VoiceAssistant import views as views1



urlpatterns = [
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("services",views.services,name='services'),
    #path("Summarizer",views.summa),
    path("Summarizer",views.summa),
    path('VoiceAssistant',views1.voice1,name='VoiceAssistant'),
    path('SpeechRecognition',views.recognition),
    
    
]