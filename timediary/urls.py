from django.urls import path

from timediary import views

urlpatterns = [
    path('', views, name='timediary')

]