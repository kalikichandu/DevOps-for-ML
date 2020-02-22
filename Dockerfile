FROM continuumio/anaconda3
MAINTAINER UNP, https://unp.education
EXPOSE 5000

RUN apt-get update && apt-get install -y vim \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/* \
 && apt-get vim

WORKDIR /usr/src/flask_predict_api/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY src/ /usr/src/flask_predict_api/

CMD gunicorn --bind 0.0.0.0:5000 wsgi:app