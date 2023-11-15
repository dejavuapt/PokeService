FROM python:3.11.2

LABEL author="KireevI.I."
LABEL version="v0.6"
LABEL paltform="web"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/pokeservice

COPY ./requirements.txt /usr/src/pokeservice/requirements.txt
RUN pip install -r /usr/src/pokeservice/requirements.txt

COPY . /usr/src/pokeservice/