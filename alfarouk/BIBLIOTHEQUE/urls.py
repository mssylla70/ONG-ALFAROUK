from django.urls import path
from . import views,livres, blocs, domaines,rayons

urlpatterns = [
    path('admin/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('resultat/<int:pk>/', views.resultat, name='resultat'),
    path('livre/<int:pk>/', livres.livre, name='livre'),
    path('edit_livre/<int:pk>/', livres.edit_livre, name='edit_livre'),
    path('supprimer_livre/<int:pk>/', livres.supprimer_livre, name='supprimer_livre'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('edit_bloc/<int:pk>/', blocs.edit_bloc, name='edit_bloc'),
    path('supprimer_bloc/<int:pk>/', blocs.supprimer_bloc, name='supprimer_bloc'),
    path('domaine/', domaines.domaine, name='domaine'),
    path('bloc/<int:pk>/', blocs.bloc, name='bloc'),  
    path('rayon/<int:pk>/', rayons.rayon, name='rayon'),
    path('edit_rayon/<int:pk>/', rayons.edit_rayon, name='edit_rayon'),
    path('supprimer_rayon/<int:pk>/', rayons.supprimer_rayon, name='supprimer_rayon'),
    path('edit_domaine/<int:pk>/', domaines.edit_domaine, name='edit_domaine'),
    path('supprimer_domaine/<int:pk>/', domaines.supprimer_domaine, name='supprimer_domaine'), 
    
]