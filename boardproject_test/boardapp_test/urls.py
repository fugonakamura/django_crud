from django.urls import path
from . import views

app_name="boardapp_test"
urlpatterns = [
    path('', views.index,name="index"),
]

