from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', include('BIBLIOTHEQUE.urls')),
    path('', include('BIBLIOTHEQUE.urls')),
    path('home', include('BIBLIOTHEQUE.urls')),
    path('edit_livre/', include('BIBLIOTHEQUE.urls')),
    path('edit_bloc/', include('BIBLIOTHEQUE.urls')),
    path('edit_rayon/', include('BIBLIOTHEQUE.urls')),
    path('edit_domaine/', include('BIBLIOTHEQUE.urls')),  
    path('login/', include('BIBLIOTHEQUE.urls')),
    path('logout/', include('BIBLIOTHEQUE.urls')),
    path('resultat/', include('BIBLIOTHEQUE.urls')),
    path('livre/', include('BIBLIOTHEQUE.urls')),
    path('bloc/', include('BIBLIOTHEQUE.urls')),
    path('rayon/', include('BIBLIOTHEQUE.urls')),
    path('domaine/', include('BIBLIOTHEQUE.urls')),
    path('supprimer_livre/', include('BIBLIOTHEQUE.urls')),
    path('supprimer_bloc/', include('BIBLIOTHEQUE.urls')),
    path('supprimer_rayon/', include('BIBLIOTHEQUE.urls')),
    path('supprimer_domaine/', include('BIBLIOTHEQUE.urls')),
    
]
