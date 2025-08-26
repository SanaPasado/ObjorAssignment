from django.urls import path
from history.views import history_list

urlpatterns = [
    path("history/", history_list, name="history_list"),
]
