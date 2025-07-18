from django.urls import include, path
from . import views


urlpatterns = [
    path('create/', views.create, name="create-page"),
    path('product-create/', views.ProductCreateList.as_view(),name="product-list-create"),
    path('product-create/<int:pk>/', views.ProductUpdateDelete.as_view(),name="product-update-delete"),

]
