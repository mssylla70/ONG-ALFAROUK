import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.db import models
from django.db.models import Sum
from .forms import *
from .models import *


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('domaine')
        else:
            return redirect('login')
    return render(request, 'login.html')
        
def logout_view(request):
    logout(request)
    return redirect('home')
           
# Home
def home(request):
    domaines = Domaines.objects.all().order_by('domaines')
    nb_livres = Livres.objects.all().aggregate(tt = Sum('exemplaires'))
    context={
        'domaines':domaines,
        'total':nb_livres,
        }
    return render(request, 'home.html', context)



# Les recherches pour les libvres
def resultat(request, pk):
    domaines   = Domaines.objects.all().order_by('domaines')
    livres  = Livres.objects.all()
    lvr = [lvr for lvr in livres if lvr.id_rayon.id_bloc.id_dom.id_dom == pk]
    le_type =Domaines.objects.get(id_dom=pk)
    total   =   0
    for nb in lvr:
        total += nb.exemplaires
    context = {
        'domaines':domaines,
        'livres': reversed(lvr),
        'total':total,
        'le_type':le_type
        }
    return render(request, 'resultat.html',context)

    
