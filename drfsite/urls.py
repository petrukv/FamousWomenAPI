"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path, re_path
from rest_framework import routers

from women import views

# router = routers.SimpleRouter()
# router.register(r'women', views.WomenViewSet, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women', views.WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', views.WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', views.WomenAPIDestroy.as_view()),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    # path('api/v1/womenlist/', views.WomenViewSet.as_view({'get':'list'})),
    # path('api/v1/womenlist/<int:pk>/', views.WomenViewSet.as_view({'put':'update'})),
    # path('api/v1/womendetail/<int:pk>/', views.WomenAPIDetailView.as_view()),

]
