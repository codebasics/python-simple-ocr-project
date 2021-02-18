FROM ubuntu:18.04


RUN apt-get update --fix-missing
RUN apt-get upgrade -y

RUN apt-get install -y libsm6 libxext6 libxrender-dev libleptonica-dev liblept5
RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential \
    && apt-get -y install python3-pip \
    && apt-get -y install software-properties-common \
    && add-apt-repository -y ppa:alex-p/tesseract-ocr \
    && apt-get -y update \
    && apt-get -y install tesseract-ocr \
    && apt-get -y install curl \
    && apt-get -y install poppler-utils

WORKDIR /project

COPY ./requirements.txt /project/requirements.txt

RUN pip3 install -r requirements.txt

COPY ./ /project/

COPY ./default /etc/nginx/sites-available/

CMD ["gunicorn", "-b", "0.0.0.0:5001", "--workers=3", "--threads=3", "-t", "90", "--error-logfile", "/project/err.log", "--log-level=debug", "wsgi:app"]
