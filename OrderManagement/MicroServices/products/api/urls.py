from django.urls import path
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Products API')

urlpatterns = [
    path('', views.home),
    path('products', views.ProductList.as_view()),
    path('products/<int:id>', views.ProductDetails.as_view()),
    path('products/docs/', schema_view)
]