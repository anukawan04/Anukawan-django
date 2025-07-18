from django.urls import path
from order import views


urlpatterns = [

    path('order-create/', views.OrderCreateList.as_view(),name='order-list-create'),
    path('order-create/<int:pk>/',views.OrderUpdateDelete.as_view(), name='order-detail'),
]
