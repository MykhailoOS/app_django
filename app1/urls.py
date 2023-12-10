
from django.urls import path, include
from .views import main


app_name = 'app1'

urlpatterns = [
    path('', main, name='home'),
]
