from django.contrib import admin

# from .forms import TimediaryCreationForm, TimediaryChangeForm
from .models import UserSetting


class UserSettingAdmin(admin.ModelAdmin):
    #  model = UserSetting
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    fields = ['user', 'repeat_period', 'start_time', 'end_time']


admin.site.register(UserSetting, UserSettingAdmin)

