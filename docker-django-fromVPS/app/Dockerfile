# base image  
FROM python:3.9.6-alpine
# setup environment variable 
ENV DockerHOME=/opt/docker/webapp/app/

# set work directory  
RUN mkdir -p $DockerHOME

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# Copy the requirement.txt file 
COPY requirements.txt $DockerHOME

# run this command to install all dependencies  
RUN pip install -r requirements.txt  

# copy whole project to your docker home directory.
COPY . $DockerHOME

EXPOSE 8000
