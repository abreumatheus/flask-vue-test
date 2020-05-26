FROM tiangolo/meinheld-gunicorn-flask:python3.8
WORKDIR /flask_api/
COPY ./flask_api/ /app

ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

RUN pip install -r /app/requirements.txt
