FROM python:3.10.6-buster
WORKDIR /server

COPY requirements_api.txt ./requirements_api.txt

RUN pip install --upgrade pip \
  && pip install -r requirements_api.txt \
  && apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY packages ./packages
COPY docker_data ./docker_data

CMD uvicorn packages.api:app --host 0.0.0.0
