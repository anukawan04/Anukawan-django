from django.urls import include, path
from . import views


urlpatterns = [
    path('create/', views.create, name="create-page"),
    path('payment-create/', views.PaymentsCreateList.as_view(),name="payment-list-create"),
    path('payment-create/<int:pk>/', views.PaymentsUpdateDelete.as_view(),name="payment-update-delete"),

]
