from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSettingSerializer
from .models import UserSetting


class UserSettingViewSet(viewsets.ModelViewSet):
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer

