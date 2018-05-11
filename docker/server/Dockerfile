FROM python:2.7.14

WORKDIR /app

COPY . /app
RUN python -m pip install -r /app/requirements.txt

COPY arc_rsa /root/.ssh/id_rsa

EXPOSE 8284
CMD ["flask", "run", "--host=0.0.0.0", "--port=8284"]
