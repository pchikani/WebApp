from django.http import HttpResponse
from .models import Products
from .serializers import ProductSerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.


def home(request):
    return HttpResponse('Hello World')


class ProductList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class ProductDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request , id):
        return self.update(request, id=id)

    def delete(self, request, id=id):
        return self.destroy(request, id=id)
