import random
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def index(request):
    user = User.objects.get(username='siner')
    return render(request, 'pythonistas/index.html', {"img": random.randrange(0, 25), "user": user})
