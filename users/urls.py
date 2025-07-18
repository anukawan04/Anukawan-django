
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('create/', views.create, name="create-page"),
    # path('user-create/', views.UsersCreateList.as_view(), name="user-list-create"),
    # path('user-create/<int:pk>/', views.UserUpdateDelete.as_view(),name="user-list-create"),
]

router = DefaultRouter()
router.register("user",views.UserViewSet)
urlpatterns += router.urls
