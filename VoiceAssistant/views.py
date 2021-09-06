from django.shortcuts import render,HttpResponse
from gtts import gTTS
import os
from django.http import JsonResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings

from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from . import ibm_services
from VoiceAssistant.ibm_services import speak,get_audio,getResponseFromAssistant


# Create your views here.
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def voice1(request):
    try:

        if request.method=='POST':
            audio1=request.FILES.get('data')
        #print(request.FILES['data'])
        # print(type(audio1))
        # print(type(audio1))  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
        # print(type(audio1.read()))  # <class 'bytes'>
        
         # <class 'str'>
            str_text = ''
        
            for line in audio1:
                str_text = str_text + line.decode()
        
        
            print(str_text)
        
            print('file has been received')

        
            mp3=gTTS(text=getResponseFromAssistant(str_text),lang='en',slow=False,tld='ca')
            print("assistant has responded")
            mp3.save("%s.wav" % os.path.join('media','web3'))
            print("the file is been saved")

    except Exception as e:
        os.remove('media/web3.wav')
        
        
        # if remove=='remove':
        #     os.remove(mp3)
        #     print('wav has been removed')
        

    
        # if text=='START':
        #     mp3=gTTS(text=getResponseFromAssistant(get_audio()),lang='en',slow=False,tld='ca')
        #     mp3.save("%s.mp3" % os.path.join('media','audio'))
            
            
            
    
    return render(request,'assistant.html')
    

# def respond():
#     mp3=gTTS(text=getResponseFromAssistant(get_audio()),lang='en')
#     mp3.save('response.mp3')
#     yield response.mp3
    
#     # #while True:
    # said=get_audio()

    # if 'stop' or 'bye' in said.split():
    #     pass#break
    # else:
    #     yield speak(getResponseFromAssistant(said))
        
    



    

    