FROM python:3.10.6-buster
WORKDIR /server

COPY requirements.txt

RUN pip install --upgrade pip \
  && pip install -r requirements_api.txt \
  && apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY packages ./packages
COPY models ./models
COPY api.py ./api.py

CMD uvicorn api:app --host 0.0.0.0 --port $PORT
