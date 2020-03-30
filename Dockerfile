FROM continuumio/anaconda3:4.4.0
MAINTAINER UNP, https://unp.education
EXPOSE 5000

RUN apt-get update && apt-get install -y vim && apt-get install -y unzip \
 && apt-get clean \
 && apt-get autoremove \
 && rm -rf /var/lib/apt/lists/* 

WORKDIR /usr/src/flask_predict_api/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


COPY CI_and_CD/src/ /usr/src/flask_predict_api/
RUN unzip models.zip -d /var/house_price_prediction/
CMD python inference.py