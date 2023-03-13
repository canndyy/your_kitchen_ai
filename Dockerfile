FROM python:3.10.6-buster
WORKDIR /server

COPY requirements_api.txt ./requirements_api.txt

RUN pip install --upgrade pip \
  && pip install -r requirements_api.txt

COPY packages ./packages

CMD uvicorn package.api:app --host 0.0.0.0
