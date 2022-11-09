from django.urls import path
from . import views

app_name = "base"
urlpatterns = [path("", views.taskList, name="tasks")]
