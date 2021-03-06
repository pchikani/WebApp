# Django rest framework as api backend for Products.

## This application allows following functionality:

01. Creating Products
02. Updating Products
03. Deleting Products


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
* /api/v1/products  -- GET method to list the available products
* /api/v1/products/<int:id>  -- GET to get specific product detials , -- PUT to update the specific product , -- DELETE to delete a specific product
* /api/v1/products/docs -- Swagger UI 
