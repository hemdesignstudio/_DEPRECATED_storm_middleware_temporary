from django.urls import path
from .views import index

app_name = "storm_middleware"

urlpatterns = [
    path('v1/index/', index, name='index'),
]
