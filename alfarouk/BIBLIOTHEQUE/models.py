from django.db import models

class Domaines(models.Model):
    id_dom    = models.AutoField(primary_key=True)
    domaines   = models.CharField(max_length=500, unique=True, null=False)
    etat       = models.CharField(max_length=1, null=False, default='t')
    
    class Meta:
        db_table = 'domaines'
            
class Auteurs(models.Model):
    id_aut     = models.AutoField(primary_key=True)
    auteur    = models.CharField(max_length=500, unique=True, null=False)
    #etat          = models.CharField(max_length=1, null=False, default='t')
    
    class Meta:
        db_table = 'auteurs'
    
class Blocs(models.Model):
    id_bloc     = models.AutoField(primary_key=True)
    bloc    = models.CharField(max_length=500, null=False)
    #etat        = models.CharField(max_length=1, null=False, default='t')
    id_dom         = models.ForeignKey(Domaines,db_column='id_dom', null=False,on_delete=models.CASCADE)
      
    class Meta:
        db_table = 'blocs'
    

    
class Rayons(models.Model):
    id_rayon   = models.AutoField(primary_key=True)
    rayon  = models.CharField(max_length=500, null=False)
    #etat       = models.CharField(max_length=1, null=False, default='t')
    id_bloc    = models.ForeignKey(Blocs,db_column='id_bloc', verbose_name=Blocs, null=False,on_delete=models.CASCADE)

    class Meta:
        db_table = 'rayons'
    
class Livres(models.Model):
    id_lv    = models.AutoField(primary_key=True)
    titre       = models.CharField(max_length=500)
    volume          = models.CharField(max_length=5)
    exemplaires = models.IntegerField(null=False)
    #etat            = models.CharField(max_length=1, null=False, default='t')
    id_aut      = models.ForeignKey(Auteurs,db_column='id_aut', null=False,on_delete=models.CASCADE)
    id_rayon    = models.ForeignKey(Rayons,db_column='id_rayon', null=False,on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'livres'
    