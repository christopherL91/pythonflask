FROM python:3.3.6

RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -
RUN apt-get install -y nodejs
RUN wget -O /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.1/dumb-init_1.0.1_amd64
RUN chmod +x /usr/local/bin/dumb-init
RUN pip install flask redis
RUN npm install -g nodemon
WORKDIR /app
ENTRYPOINT ["dumb-init"]
