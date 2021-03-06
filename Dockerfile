FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository -y ppa:alex-p/tesseract-ocr
RUN apt-get update && apt-get install -y tesseract-ocr-all libsm6 libxext6 libxrender-dev

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir app
RUN mkdir uploads
run cd app
COPY ./requirements.txt requirements.txt
COPY ./*.py ./ 
RUN pip3 install -r requirements.txt
ENTRYPOINT python3 main.py
