from django.urls import path
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Orders API')

urlpatterns = [
    path('', views.home),
    path('orders', views.OrderList.as_view()),
    path('orders/<int:id>', views.OrderDetails.as_view()),
    path('orders/docs/', schema_view),
]