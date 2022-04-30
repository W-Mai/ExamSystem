import time

from django.shortcuts import render
import random


# Create your views here.
def home(request):
    name = request.session.get('name', None)
    if name is None:
        name = str(time.time())
        request.session['name'] = name

    return render(request, 'home.html', {
        'name': name,
    })
