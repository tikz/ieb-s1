FROM python:3.10-alpine

RUN apk add git build-base python3 py3-pip 
RUN pip install pipenv

RUN mkdir -p /iebs1
COPY . /iebs1/
WORKDIR /iebs1
RUN pipenv install --system --deploy

ENTRYPOINT ["python", "client.py"]
