from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
#from custom_auth.forms import MyUserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import MyUserCreationForm
from django.http import HttpResponseRedirect

# Create your views here.

app_name="custom_auth"
def signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            phone_number = form.cleaned_data.get('phone_number')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(phone_number=phone_number, password=raw_password)
            login(request, user)
            return render(request, "posts/post_list.html")
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})