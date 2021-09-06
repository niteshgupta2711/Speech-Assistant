FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY . /code/
RUN apt-get -y update && apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y && pip install PyAudio && pip install -r requirements.txt 

