FROM python:2.7.14

COPY . /celery
RUN python -m pip install -r /celery/requirements.txt

COPY arc_rsa /root/.ssh/id_rsa

WORKDIR /app
