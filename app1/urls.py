
from django.urls import path, include
from .views import main


app = 'main'

urlpatterns = [
    path('', main, name='home'),
]
