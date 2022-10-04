FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install gunicorn -y

WORKDIR /usr/src/app

ADD requirements.txt .
RUN pip install -r requirements.txt
COPY . .
#RUN apt install -y postgresql postgresql-contrib postgresql-client
#  #need postgresql to be installed, in macos do : brew install postgresql
RUN apt-get update
ENTRYPOINT [ "python" ]

CMD [ "wsgi.py" ]

#docker build -t lookup_data_api .
#docker network create db
#docker run -d -p 5001:5001 --name lookup_data_api --restart=always lookup_data_api:latest