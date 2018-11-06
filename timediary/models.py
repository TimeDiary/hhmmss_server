from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class Settings(models.Model):
    # User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # 반복 주기
    repeat_period = models.PositiveIntegerField(default=60)

    # 반복 시작 시간
    start_time = models.TimeField(default='09:00')
    # 반복 종료 시간
    end_time = models.TimeField(default='18:00')
