FROM python:2.7
MAINTAINER Simon Gareste <simon.gareste@arturia.com>

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD [ "python", "./wsgi.py" ]
