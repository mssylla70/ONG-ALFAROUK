from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Domaines, Livres, Auteurs, Rayons,Blocs
from .forms import AuteursForm, LivresForm, BlocsForm, RayonsForm, DomainesForm
from django.contrib.auth import authenticate, login
import datetime

@login_required
def livre(request, pk):
    domaines    = Domaines.objects.all().order_by('domaines')
    livres      = Livres.objects.filter(id_rayon=pk)
    le_type     = Rayons.objects.get(id_rayon=pk)
    ryon = Rayons.objects.get(id_rayon=pk)
    
    total       =   0
    for nb in livres:
        total += nb.exemplaires
        
    form = LivresForm()
    if request.method=='POST':
        
        auteur = request.POST.get('auteur')
        vlm    = request.POST.get('volume')
        titre  = request.POST.get('titre')
        exemp  = request.POST.get('exemplaires')
        if not vlm:
            vlm = ' '
        try:
            Auteurs.objects.create(auteur=auteur)
        except:
            pass
        
        aut = Auteurs.objects.get(auteur=auteur)
        ryn = Rayons.objects.get(id_rayon=pk)
        form.instance.id_aut       = aut
        form.instance.titre        = titre
        form.instance.volume       = vlm
        form.instance.exemplaires  = exemp
        form.instance.id_rayon     = ryn
        
        if form.is_valid:
            try:
                form.save()
            except:
               pass
            
            return redirect('/livre/'+str(pk))
            
    context = {
        'domaines':domaines,
        'livres': reversed(livres),
        'total':total,
        'le_type':le_type,
        'form':form,
        'ryon':ryon,
        }
    return render(request, 'livre.html',context)

@login_required
def edit_livre(request, pk):
    data 	= Livres.objects.get(id_lv=pk)
    domaines   = Domaines.objects.all().order_by('domaines')
    rayons  = Rayons.objects.all().order_by('rayon')
    form    = LivresForm(instance=data)
    if request.method == "POST":   
        auteur      = request.POST.get('auteur')
        vlm         = request.POST.get('volume')
        if not vlm:
            vlm = ' '
        try:
            Auteurs.objects.create(auteur=auteur)
        except:
            pass
        
        aut = Auteurs.objects.get(auteur=auteur)
        data.volume = vlm
        data.id_aut = aut
        
        form    = LivresForm(request.POST, instance=data)
        if form.is_valid():
            try:
                form.save()
            except:
                pass
            return redirect('/livre/'+str(data.id_rayon.id_rayon))
    context = { "form": form, 'domaines': domaines, 'rayons': rayons, 'data':data}
    return render(request, "edit_livre.html", context)

@login_required
def supprimer_livre(request, pk):
    livre       =   Livres.objects.get(id_lv=pk)
    lve     = livre.id_rayon.id_rayon
    livre.delete()
    return redirect('/livre/'+str(lve))