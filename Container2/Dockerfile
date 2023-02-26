FROM python:3.9-slim-buster

WORKDIR /data

COPY ./data

EXPOSE 5000

RUN pip install --trusted-host pypi.python.org -r requirements.txt

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0"]

MAINTAINER dozie
