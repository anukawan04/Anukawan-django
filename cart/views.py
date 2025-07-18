

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Cart
from .serializer import CartSerializer
from rest_framework import status


# Create your views here.


def create(request):
    return HttpResponse("This is a create page")


class CartsCreateList(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def delete(self, request, *args, **kwargs):
        Cart.objects.all().delete()
        return Response(status=status.HTTP_204_No_CONTENT)


class CartsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "pk"
