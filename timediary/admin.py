from django.contrib import admin

# from .forms import TimediaryCreationForm, TimediaryChangeForm
from .models import Settings


class SettingsAdmin(admin.ModelAdmin):
    #  model = Settings
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    fields = ['user', 'repeat_period', 'start_time', 'end_time']


admin.site.register(Settings, SettingsAdmin)

