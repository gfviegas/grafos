FROM python:3

RUN mkdir /code
WORKDIR /code

COPY . /code
RUN pip install --upgrade pip
RUN pip install -e .
