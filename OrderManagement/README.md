# Microservices architecture based web application wth individual modules and database.

## This application allows following functionality:

01. Creating / Updating / Deleting Products
02. Creating / Updating / Deleting Products Categories
03. Creating / Updating / Deleting Orders


* Above 3 api modules are created using Django Rest Framework and using docker these application can be scaled based on requirement.
* All 3 api modules have independent database created in mongodb.
* Nginx is used as web server to publish all the api endpoints.
* All individual api endpoints are documented in Swagger UI.
* All api modules , database and nginx web server are created using docker-compose.

## Technology Stack:
01. Python
02. Django/Django REST Framework
03. Mongodb
04. Nginx
05. Docker
06. Swagger UI


## For testing:
01. Clone the repo
02. Run "docker-compose build" while inside the microservices folder
03. After docker completes all the building stuffs, run "docker-compose up -d" to run each microservices.
04. Now go to your localhost, docker machine ip or server ip to access the API endpoints.
05. Endpoints details can be pulled using /api/v1/< products / orders / category >/docs 
