FROM python:3.11-bookworm

RUN apt-get update && apt-get install -y redis

RUN pip3 install saq aiohttp==3.9.3

WORKDIR /app
