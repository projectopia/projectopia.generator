FROM python:3.9-alpine

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
COPY . .
RUN \
  pip install -r requirements.txt
  
ENTRYPOINT [ "python3", "wsgi.py" ]
