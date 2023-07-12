FROM ubuntu:22.04

COPY ./src /app

COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt