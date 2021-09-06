from django.contrib import admin
from django.urls import path
from VoiceAssistant import views

urlpatterns = [
    
    path('VoiceAssistant',views.voice1,name="VoiceAssistant"),

]