FROM python:3.8.6-slim
MAINTAINER LonelyCloud Ltd

ENV PYTHONBUFFERED 1

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src