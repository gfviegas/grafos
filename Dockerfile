FROM python:3

RUN pip install Sphinx
RUN pip install rinohtype

RUN mkdir /code
WORKDIR /code

COPY . /code
RUN pip install -e .
