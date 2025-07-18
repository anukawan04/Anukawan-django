# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
from rest_framework import status


# Create your views here.


def create(request):
    return HttpResponse("This is a create page")


class ProductCreateList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def delete(self, request, *args, **kwargs):
        Product.objects.all().delete()
        return Response(status=status.HTTP_204_No_CONTENT)


class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
