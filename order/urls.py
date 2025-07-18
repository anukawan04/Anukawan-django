from django.urls import path
from order import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    # path('create/', views.create, name="create-page"),
    # path('order-create/', views.OrderCreateList.as_view(),name='order-list-create'),
    # path('order-create/<int:pk>/',views.OrderUpdateDelete.as_view(), name='order-detail'),
]


router = DefaultRouter()
router.register("order", views.UserViewSet)
urlpatterns += router.urls
