FROM python:3.11.6

# ENV PYTHONUNBUFFERED=1

WORKDIR /code

RUN apt update -y

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .