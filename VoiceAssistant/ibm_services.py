
import os
import time


from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import AssistantV2
import json


# text_speech = pyttsx3.init()
# rate = text_speech.getProperty('rate')
# text_speech.setProperty('rate', rate-4)
# text_speech.say('The quick brown fox jumped over the lazy dog.')
# text_speech.runAndWait()
# engine = pyttsx3.init()
# engine=pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     engine.setProperty('voice', voice.id)
#     print(voice)
#     engine.runAndWait()
# text_speech=pyttsx3.init()
#     text_speech.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    
#     text_speech.say(Txt)
#     text_speech.runAndWait()






def speak(Txt):
    pass   
    
    
    
    


    
    
def get_audio(path):
    r=sr.Recognizer()
    with sr.WavFile(path) as source:
        audio=r.record(source)
    return r.recognize_google(audio)


assistant_api='-SEKswVD3hButgeTPHAnzjVVALeMFs_uLz4xkTX3FRYF'
assistant_url='https://api.jp-tok.assistant.watson.cloud.ibm.com/instances/2aab33dd-7245-4307-b67a-9c2eee92faaa'
ASSISTANT_ID='ed4bacc3-4e94-4bd2-8040-9ed10b64dd5d'


#response=assistant.get_workspace(workspace_id=ASSISTANT_ID).get_result()
def getResponseFromAssistant(chat_text):
    assistant=AssistantV2(version='2019-02-28',authenticator=IAMAuthenticator(assistant_api))
    assistant.set_service_url(assistant_url)
    session=assistant.create_session(assistant_id =ASSISTANT_ID)
    session_id=session.get_result()["session_id"]
    response=assistant.message(assistant_id=ASSISTANT_ID,session_id=session_id, input={'message_type': 'text','text': chat_text}).get_result()
    response_text = response["output"]["generic"][0]["text"]

    return response_text


    #speak(getResponseFromAssistant(get_audio()))













