from django.urls import path
from .views import addStudent
urlpatterns=[
    path("",addStudent,name="allforms"),
]