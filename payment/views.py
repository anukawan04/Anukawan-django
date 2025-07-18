# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Payment
from .serializer import PaymentSerializer
from rest_framework import status


# Create your views here.


def create(request):
    return HttpResponse("This is a create page")


class PaymentsCreateList(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def delete(self, request, *args, **kwargs):
        Payment.objects.all().delete()
        return Response(status=status.HTTP_204_No_CONTENT)


class PaymentsUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    lookup_field = "pk"
