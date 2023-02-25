FROM python:3.9-slim-buster

WORKDIR /tmp

COPY . .

EXPOSE 8080

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "user_app.py"]
