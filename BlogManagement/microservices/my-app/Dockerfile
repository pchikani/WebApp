FROM node:14.17.3-alpine

RUN mkdir /code

WORKDIR /code

COPY package.json .

RUN npm install

COPY . .

