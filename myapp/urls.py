"""
URL configuration for myapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from ecommerce import urls as ecommerce_urls
from payment import urls as payment_urls
from users import urls as users_urls
from order import urls as order_urls
from products import urls as products_urls
from cart import urls as cart_urls

import myapp.my_admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce/', include(ecommerce_urls)),
    path('api/v1/',include(users_urls)),
    path('api/v2/',include(payment_urls)),
    path('api/v3/', include(order_urls)),
    path('api/v4/',include(products_urls)),
    path('api/v5/', include(cart_urls)),

   

]
