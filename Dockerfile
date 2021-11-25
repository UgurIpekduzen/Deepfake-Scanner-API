FROM ubuntu:18.04

RUN apt-get update
RUN apt-get dist-upgrade -y
RUN apt-get install software-properties-common -y 
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.7 -y

RUN apt-get update
RUN apt-get install python3-pip -y

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx -y

COPY ./src /app/src 
COPY ./weights /app/weights 
COPY config.json /app
COPY main.py /app
COPY ./requirements.txt /app

WORKDIR /app

RUN python3.7 -m pip install --upgrade pip; pip install -r requirements.txt

EXPOSE 8000
  
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]  

# çalıştırmak için: docker run -p 8000:8000 <container-id>
