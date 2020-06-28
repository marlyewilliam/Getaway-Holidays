"""GetawayHolidays URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from getawayHolidays import views
from django.conf.urls import url
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet),
router.register(r'staff-reservation', views.StaffReservation),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path(r'', include(router.urls)),
    url(r'^api-token-auth/', obtain_auth_token),
    url(r'^logout/', views.Logout.as_view()),
    url(r'^user-reservation/', views.UserReservation.as_view()),
    url('reservation/(?P<pk>[0-9]+)/', views.Reservation.as_view()),


]
