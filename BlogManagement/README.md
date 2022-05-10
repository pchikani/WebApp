# Microservices architecture based web application with reactjs as frontend and django rest framework as api backend.

## This application allows following functionality:

01. Creating User
02. Change Password
03. Passowrd and Token based authentication
04. Admin panel for user management
05. Creating blog articles 
06. Updating blog articles
07. Deleting blog articles

## Technology Stack:
01. reactjs 
02. python
03. Django/Django REST Framework
04. Nginx
05. Docker
06. Swagger UI

Python used as the backend development language. Django used as the backend framework. Django REST Framework or DRF used as the REST API development framework, 
default SQLlite used as the database backend, reactjs as frontend , Nginx used as the API gateway and finally docker used as the deployment method. 
Swagger used for documenting API

Nginx sits in front of each of the services to abstract all the microservices API endpoints into single one.

## For testing:
01. Clone the repo
02. Run "docker-compose build" while inside the microservices folder
03. After docker completes all the building stuffs, run "docker-compose up -d" to run each microservices.
04. Now go to your localhost, docker machine ip or server ip to access the API endpoints at port 8000.
05. Or use reactjs frontend to login and work with articles at port 3000.
