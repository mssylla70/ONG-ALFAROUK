import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import (AuteursForm, BlocsForm, LivresForm, RayonsForm, DomainesForm)
from .models import (Auteurs, Blocs, Livres, Rayons, Domaines)



@login_required
def rayon(request, pk):
    domaines = Domaines.objects.all().order_by('domaines')
    rayons = Rayons.objects.filter(id_bloc=pk).order_by('rayon')
    blo = Blocs.objects.get(id_bloc=pk)
    form = RayonsForm()
    if request.method=='POST':
        form = RayonsForm(request.POST)        
        form.instance.id_bloc = Blocs.objects.get(id_bloc=pk)
        if form.is_valid:
            form.save()
            return redirect('/rayon/'+str(blo.id_bloc))
    context = {
        'domaines':domaines,
        'rayons': rayons,
        'form': form,
        'blo':blo,
        }
    return render(request, 'rayons.html',context)


@login_required
def edit_rayon(request, pk):
    data 	= Rayons.objects.get(id_rayon=pk)
    domaines = Domaines.objects.all().order_by('domaines')
    form    = RayonsForm(instance=data)
    if request.method == "POST":  
        form    = RayonsForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('/rayon/'+str(data.id_bloc.id_bloc))
    context = { "form": form, 'domaines' :domaines, 'id_bloc':data.id_bloc.id_bloc}
    return render(request, "edit_rayon.html", context)

@login_required
def supprimer_rayon(request, pk):
    rayon      =   Rayons.objects.get(id_rayon=pk)
    ray     = rayon.id_bloc.id_bloc
    rayon.delete()
    return redirect('/rayon/'+str(ray))