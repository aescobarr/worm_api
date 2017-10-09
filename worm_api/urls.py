"""worm_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'wormuser', views.WormUserViewSet, base_name='wormuser')
router.register(r'scenario', views.ScenarioViewSet, base_name='scenario')
router.register(r'obstacle', views.ObstacleViewSet, base_name='obstacle')
router.register(r'decor', views.DecorViewSet, base_name='decor')
router.register(r'bacterium', views.BacteriumViewSet, base_name='bacterium')
router.register(r'action', views.ActionViewSet, base_name='action')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/',include(router.urls)),
    url(r'^api/user_auth/', views.api_login, name='user_auth'),
]
