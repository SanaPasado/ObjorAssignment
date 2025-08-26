# tweets/urls.py

from django.urls import path

from .views import TweetDetailView, TweetListView, TweetCreateView

urlpatterns = [
    # Path for creating a new tweet
    path('create/', TweetCreateView.as_view(), name='tweet_create'),

    path('', TweetListView.as_view(), name='tweet_list'),

    path('<int:pk>/', TweetDetailView.as_view(), name='tweet_detail'),
]
