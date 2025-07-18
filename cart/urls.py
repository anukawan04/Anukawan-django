from django.urls import include, path
from . import views


urlpatterns = [
    path('create/', views.create, name="create-page"),
    path('cart-create/', views.CartsCreateList.as_view(), name="cart-list-create"),
    path('cart-create/<int:pk>/', views.CartsUpdateDelete.as_view(),name="cart-update-delete"),
]
