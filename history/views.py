from django.shortcuts import render
from .models import History

def history_list(request):
    histories = History.objects.all().order_by("-date")
    return render(request, "history.html", {"histories": histories})
