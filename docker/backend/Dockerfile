#defining dockerfile for our sever applciations. tried 3.9,3.6
#FROM ubuntu:xenial
FROM python:3.8-slim-buster

# RUN apt-get update && \
#     apt-get install -y software-properties-common && \
#     add-apt-repository ppa:deadsnakes/ppa && \
#     apt-get update && \
#     apt-get install -y python3.7 python3.7-dev python3-pip
# RUN brew update && \
#     brew install -y software-properties-common && \
#     add-apt-repository ppa:deadsnakes/ppa && \
#     brew update && \
#     brew install -y python3.7 python3.7-dev python3-pip
# RUN brew update && \
#     brew install python@3.7

WORKDIR /app
COPY requirements.txt .
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.9 /usr/bin/python
RUN rm -f /usr/bin/python3 && ln -s /usr/bin/python3.9 /usr/bin/python3
RUN set -xe \
    && apt-get update -y \
    && apt-get install -y python3-pip
# RUN pip3 install -r requirements.txt
# RUN pip3 install gunicorn==19.9.0
# RUN /usr/local/bin/python -m pip install --upgrade pip && \
#     pip3 install -e .
#RUN apk add py3-pip
#RUN pip install --upgrade pip
RUN pip install --upgrade Cython
RUN pip install -r requirements.txt
RUN pip install gunicorn==19.9.0

ADD ./backend /app/backend
ADD ./docker /app/docker
ADD ./research /app/research

RUN chmod +x /app/docker/backend/wsgi-entrypoint.sh
RUN mkdir -p /app/backend/server/static
