FROM ubuntu:20.04

RUN apt-get update \
    && apt-get install -y python \
    && apt-get install -y python3-pip \
    && pip install flask \
    && pip install flask-mysql
COPY app.py /opt/app.py
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0
