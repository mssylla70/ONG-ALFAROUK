# Generated by Django 4.1.1 on 2022-09-12 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auteurs',
            fields=[
                ('id_auteur', models.AutoField(primary_key=True, serialize=False)),
                ('nom_auteur', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'auteurs',
            },
        ),
        migrations.CreateModel(
            name='Blocs',
            fields=[
                ('id_bloc', models.AutoField(primary_key=True, serialize=False)),
                ('nom_bloc', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'blocs',
            },
        ),
        migrations.CreateModel(
            name='Emprunteurs',
            fields=[
                ('id_emprunteur', models.AutoField(primary_key=True, serialize=False)),
                ('prenom', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'emprunteurs',
            },
        ),
        migrations.CreateModel(
            name='Rayons',
            fields=[
                ('id_rayon', models.AutoField(primary_key=True, serialize=False)),
                ('nom_rayon', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'rayons',
            },
        ),
        migrations.CreateModel(
            name='Type_livres',
            fields=[
                ('id_type', models.AutoField(primary_key=True, serialize=False)),
                ('nom_type', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'type_livres',
            },
        ),
        migrations.CreateModel(
            name='Livres',
            fields=[
                ('id_livre', models.AutoField(primary_key=True, serialize=False)),
                ('nom_livre', models.CharField(max_length=500)),
                ('volume', models.CharField(max_length=5)),
                ('id_auteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BIBLIOTHEQUE.auteurs')),
                ('id_bloc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BIBLIOTHEQUE.blocs')),
                ('id_rayon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BIBLIOTHEQUE.rayons')),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BIBLIOTHEQUE.type_livres')),
            ],
            options={
                'db_table': 'livres',
            },
        ),
        migrations.CreateModel(
            name='Emprunts',
            fields=[
                ('id_emprunt', models.AutoField(primary_key=True, serialize=False)),
                ('date_emprunt', models.DateField(auto_now=True)),
                ('date_retour', models.DateField(null=True)),
                ('etat', models.BooleanField(default='false')),
                ('id_emprunteur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BIBLIOTHEQUE.emprunteurs')),
                ('id_livre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BIBLIOTHEQUE.livres')),
            ],
            options={
                'db_table': 'emprunts',
            },
        ),
    ]