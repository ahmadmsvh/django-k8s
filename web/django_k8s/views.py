from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.http import HttpResponse


# Create your views here.

def portfolio(request):
    response = '''<div style="display: flex; align-items: center;
justify-content: center;"><div style="width:70%;"><img src='https://django-k8s.ams3.digitaloceanspaces.com/static/Ahmad-MousaviHaghdoust.jpg' alt="" style="height: 100px; float: left;">
<div style="height: 100px; background-color: rgb(92, 132, 192); display: flex; align-items: center;
justify-content: center;">
    <h1 style="color: aliceblue;">This is going to become a fabulous blog for programmrs</h1>
</div>
<div style="height: 100px; background-color: rgb(57, 77, 107); display: flex; align-items: center;
justify-content: center;">
    <h1 style="color: aliceblue;">django/devops</h1>
</div></div><div/>
'''
    # cats_load.run() 
    return HttpResponse(response)