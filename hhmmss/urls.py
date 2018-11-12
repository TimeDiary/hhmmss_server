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

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView

router = routers.DefaultRouter()
router.register(r'UserSetting', timediaryViews.UserSettingViewSet)


# rest_auth
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


urlpatterns = [
    # testpage
    path('testpage/', include('tespage.urls')),

    # allauth
    path('accounts/', include('allauth.urls')),

    # rest_auth
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/google/', GoogleLogin.as_view(), name='google_login'),

    # Django Admin
    path('admin/', admin.site.urls),

    # TimeDiary
    # path('timediary/', include('timediary.urls')),

    # DRF
    path('', include(router.urls)),
]
