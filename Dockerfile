FROM python:alpine3.15

EXPOSE 5000

RUN mkdir /flask_app

WORKDIR /flask_app

COPY . /flask_app

ENV FLASK_APP=flask_simple_api.app
ENV FLASK_ENV=development

RUN pip install -r requirements.txt

CMD flask run --host "0.0.0.0"
