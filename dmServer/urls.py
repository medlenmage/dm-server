from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from dmApi.views import register_dmuser, login_user
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_dmuser),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('login', login_user),
]
