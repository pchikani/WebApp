# Django rest framework as api backend for Product Categories.

## This application allows following functionality:

01. Creating Products Categories
02. Updating Products Categories
03. Deleting Products Categories


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
/api/v1/category  -- GET method to list the available products category
/api/v1/category/<int:id>  -- GET to get specific product category detials , -- PUT to update the specific product category , -- DELETE to delete a specific product category
/api/v1/category/docs -- Swagger UI 