from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HomeView

app_name='blog'

urlpatterns = [
    path('blog/', HomeView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)