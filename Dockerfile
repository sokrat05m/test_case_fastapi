FROM python:3.12-alpine3.18


COPY requirements.txt /temp/requirements.txt
COPY src /src
WORKDIR /src
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password sokrat

USER sokrat