from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Users
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializer import UserSerializer


# Create your views here.


def create(request):
    return HttpResponse("This is a create page")

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def delete(self, request, *args, **kwargs):
        Users.objects.all().delete()
        return Response(status=status.HTTP_204_N0_CONTENT)




# class UsersCreateList(generics.ListCreateAPIView):
#     queryset = Users.objects.all();
#     serializer_class = UserSerializer;

#     def delete(self, request, *args , **kwargs):
#         Users.objects.all().delete()
#         return Response(status=status.HTTP_204_N0_CONTENT)

# class UserUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Users.objects.all();
#     serializer_class = UserSerializer;
#     lookup_field = "pk" #primarykey

