from django.urls import path
from . import views

urlpatterns = [
    path("attempts/", views.attempt_history, name="attempt-history"),
]
