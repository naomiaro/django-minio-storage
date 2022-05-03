FROM python:3.9.10

ENV PYTHONUNBUFFERED=1

RUN mkdir /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
