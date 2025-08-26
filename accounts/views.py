from django.contrib.auth import login
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm, LoginForm


# Create your views here.
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        new_user = form.save(commit=False)  # don't save yet
        new_user.set_password(form.cleaned_data["password"])  # hash password
        new_user.save()  # now save to DB
        return redirect("login")

    return render(request, "register.html", context)

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form}

    if form.is_valid():
        user = form.cleaned_data["user"]
        login(request, user)
        return redirect('tweets:tweet_list')



    return render(request, 'login.html', context)