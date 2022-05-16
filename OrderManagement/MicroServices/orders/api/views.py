from django.http import HttpResponse
from .models import Orders
from .serializers import OrderSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.


def home(request):
    return HttpResponse('Order Home')


class OrderList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class OrderDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request , id):
        return self.update(request, id=id)

    def delete(self, request, id=id):
        return self.destroy(request, id=id)
