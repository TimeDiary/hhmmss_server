"""TimeDiary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.urls import path, include
from rest_framework import routers
from timediary import views as timediaryViews

router = routers.DefaultRouter()
router.register(r'UserSetting', timediaryViews.UserSettingViewSet)

urlpatterns = [
    # Main
    path('testpage/', include('tespage.urls')),

    # Django Admin
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),

    # Django Admin
    path('admin/', admin.site.urls),

    # TimeDiary
    # path('timediary/', include('timediary.urls')),

    # DRF
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls'))

]
