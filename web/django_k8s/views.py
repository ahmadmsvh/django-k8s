from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import View
from django.http import HttpResponse


# Create your views here.

def portfolio(request):
    response = '''<img src="../../k8s/nginx-test/statics/statics/d20230107_194548.jpg" alt="" style="height: 100px; float: left;">
<div style="height: 100px; background-color: rgb(92, 132, 192); display: flex; align-items: center;
justify-content: center;">
    <h1 style="color: aliceblue;">This is going to be a fabulous blog for programmrs</h1>
</div>
'''
    # cats_load.run() 
    return HttpResponse(response)