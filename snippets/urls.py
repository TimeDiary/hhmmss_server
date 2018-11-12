from django.urls import path

from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('locations/', views.LocationList.as_view()),
    path('locations/(<pk>[0-9]+)/', views.UserDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/(<pk>[0-9]+)/', views.UserDetail.as_view()),
    path('login/', views.Login.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
