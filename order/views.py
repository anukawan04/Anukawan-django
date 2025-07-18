from rest_framework import generics
from .serializer import OrderSerializer
from .models import Order
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        Order.objects.all().delete()
        return Response(status=status.HTTP_204_N0_CONTENT)


# class OrderCreateList(generics.ListCreateAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer


# class OrderUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer
#     lookup_field = 'pk'
