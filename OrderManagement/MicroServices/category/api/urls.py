from django.urls import path
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Category API')


urlpatterns = [
    path('', views.home),
    path('category', views.CategoryList.as_view()),
    path('category/<int:id>', views.CategoryDetails.as_view()),
    path('category/docs/', schema_view),
]