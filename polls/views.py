from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


from .models import Bunk, User
# Create your views here.
bunk_list = Bunk.objects.all().order_by('time')

names = set()
for bunk in bunk_list:
    names.add(bunk.from_user)
    names.add(bunk.to_user)
names = list(names)

def index(request):
    return render(request, 'homepage.html', {'bunk_list': bunk_list, "names": names})

def detail(request, name):

    return render(request, 'about.html', {'bunk_list': bunk_list, 'name': name})

def add_bunk(request):
    from_user = request.POST.get('from_user')
    to_user = request.POST.get('to_user')
    from_user = User.objects.get(username=from_user)
    to_user = User.objects.get(username=to_user)
    new_bunk = Bunk(from_user=from_user, to_user=to_user, time=datetime.now())

    new_bunk.save()
    return render(request, 'homepage.html', {'bunk_list': Bunk.objects.all().order_by('time'), 'names': names})