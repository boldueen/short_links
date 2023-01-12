FROM python:3.11

ENV PYTHONPATH "${PYTHONPATH}:/code"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

COPY . /code/

COPY requirements.txt /code/
RUN pip install -r requirements.txt

