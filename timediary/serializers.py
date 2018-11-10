from .models import UserSetting
from rest_framework import serializers


class UserSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserSetting
        fields = ('user', 'repeat_period', 'start_time', 'end_time')
        # fields = ('repeat_period', 'start_time', 'end_time')


