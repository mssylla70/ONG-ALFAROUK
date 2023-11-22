import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import (AuteursForm, BlocsForm,
                    LivresForm, RayonsForm, DomainesForm)
from .models import (Auteurs, Blocs, Livres, Rayons,
                     Domaines)

def domaine(request):
    domaines = Domaines.objects.all().order_by('domaines')
    form = DomainesForm()
    if request.method=='POST':
        form = DomainesForm(request.POST)
        if form.is_valid:
            form.save()
    if request.user.is_authenticated:
        return render(request, 'domaine.html', {'domaines':domaines,'form':form})
    return redirect('login')

@login_required
def edit_domaine(request, pk):
    data 	= Domaines.objects.get(id_dom=pk)
    domaines   = Domaines.objects.filter(etat='t').order_by('domaines')
    form    = DomainesForm(instance=data)
    if request.method == "POST":   
        form    = DomainesForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('domaine')
    context = { "form": form, 'domaines' :domaines}
    return render(request, "edit_domaine.html", context)

@login_required
def supprimer_domaine(request, pk):
    domaine   =   Domaines.objects.get(id_dom=pk)
    domaine.delete()
    return redirect('/domaine/')