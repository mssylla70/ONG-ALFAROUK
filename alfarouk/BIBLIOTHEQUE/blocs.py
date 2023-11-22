import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import (AuteursForm, BlocsForm,  LivresForm, RayonsForm, DomainesForm)
from .models import (Auteurs, Blocs,  Livres, Rayons, Domaines)

@login_required
def bloc(request, pk):
    domaines = Domaines.objects.all().order_by('domaines')
    blocs = Blocs.objects.filter(id_dom=pk).order_by('bloc')
    dom = Domaines.objects.get(id_dom=pk)
    
    form = BlocsForm()
    if request.method=='POST':
        form = BlocsForm(request.POST)
        form.instance.id_dom = Domaines.objects.get(id_dom=pk)
        if form.is_valid:
            form.save()
            return redirect('/bloc/'+str(pk))
            
    context = {
        'domaines':domaines,
        'blocs': blocs,
        'form':form,
        'dom':dom,
        }
    return render(request, 'blocs.html',context)

    
@login_required
def edit_bloc(request, pk):
    data 	= Blocs.objects.get(id_bloc=pk)
    domaines = Domaines.objects.all().order_by('domaines')
    bl = Blocs.objects.get(id_bloc=pk)
    
    form    = BlocsForm(instance=data)
    if request.method == "POST": 
        form    = BlocsForm(request.POST, instance=data)
        if form.is_valid():
            form.save()            
            return redirect('/bloc/'+str(data.id_dom.id_dom))
    context = { "form": form, 'domaines' :domaines, 'id_dom':bl.id_dom.id_dom}
    
    return render(request, "edit_bloc.html", context)

@login_required
def supprimer_bloc(request, pk):
    bloc      =   Blocs.objects.get(id_bloc=pk)
    blc     = bloc.id_dom.id_dom
    bloc.delete()
    return redirect('/bloc/'+str(blc))