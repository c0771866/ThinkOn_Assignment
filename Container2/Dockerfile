FROM python:3

WORKDIR /usr/src/app

COPY . .

EXPOSE 5000

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP app.py

CMD ["flask", "run", "--host=0.0.0.0", "shift.py]

MAINTAINER dozie
