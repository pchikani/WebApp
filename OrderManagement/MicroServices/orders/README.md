# Django rest framework as api backend for Product Orders.

## This application allows following functionality:

01. Creating Products Orders
02. Updating Products Orders
03. Deleting Products Orders


## Technology Stack:
01. python
02. Django/Django REST Framework
03. Mongodb
04. Docker
05. Swagger UI

Python used as the backend development language. Django used as the backend framework. Django REST Framework or DRF used as the REST API development framework, 
Mongodb used as the database backend, docker used as the deployment method for creating scaleable api module within the project.
Swagger used for documenting API


## URLS for testing:
/api/v1/orders  -- GET method to list the available orderss
/api/v1/orders/<int:id>  -- GET to get specific orders detials , -- PUT to update the specific orders , -- DELETE to delete a specific orders
/api/v1/orders/docs -- Swagger UI 