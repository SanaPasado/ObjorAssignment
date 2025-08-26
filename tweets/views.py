from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from history.models import History
from tweets.forms import TweetModelForm
from .models import Tweet

class TweetListView(ListView):
    model = Tweet
    template_name = 'list.html'
    context_object_name = 'tweets'
    queryset = Tweet.objects.all().order_by('-created_at')

    def get_context_data(self, **kwargs):
        # First, get the default context from the parent class
        context = super().get_context_data(**kwargs)
        # Then, add the history records to that context
        context['history_records'] = History.objects.all().order_by('-date')
        return context


class TweetDetailView(DetailView):
    model = Tweet
    template_name = 'detail.html'
    context_object_name = 'tweet'

    def get_object(self, queryset=Tweet.objects.all()):
        return Tweet.objects.get(pk=self.kwargs['pk'])


class TweetCreateView(CreateView):
    model = Tweet
    form_class = TweetModelForm
    template_name = 'create.html'
    context_object_name = 'tweet_create'
    success_url = reverse_lazy('tweets:tweet_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)

