from django.http import HttpResponse
from .models import Category
from .serializers import CategorySerializer
from rest_framework import mixins
from rest_framework import generics

# Create your views here.


def home(request):
    return HttpResponse('Category Home')


class CategoryList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CategoryDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request , id):
        return self.update(request, id=id)

    def delete(self, request, id=id):
        return self.destroy(request, id=id)
