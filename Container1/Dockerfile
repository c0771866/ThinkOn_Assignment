FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./

EXPOSE 8080

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "user_app.py"]

MAINTAINER dozie
