# Generated by Django 3.1 on 2020-08-11 14:55

import aidants_connect.apps.mandats.models
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aidants', '0001_initial'),
        ('usagers', '__first__'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=None,
            state_operations=[


                migrations.CreateModel(
                    name='Autorisation',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('demarche', models.CharField(choices=[('papiers', 'Papiers - Citoyenneté'), ('famille', 'Famille'), ('social', 'Social - Santé'), ('travail', 'Travail'), ('logement', 'Logement'), ('transports', 'Transports'), ('argent', 'Argent'), ('justice', 'Justice'), ('etranger', 'Étranger'), ('loisirs', 'Loisirs')], max_length=16)),
                        ('revocation_date', models.DateTimeField(blank=True, null=True, verbose_name='Date de révocation')),
                        ('last_renewal_token', models.TextField(default='No token provided')),
                    ],
                    options={
                        'db_table': 'aidants_connect_web_autorisation',
                    },
                ),
                migrations.CreateModel(
                    name='Mandat',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de création')),
                        ('expiration_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'expiration")),
                        ('duree_keyword', models.CharField(choices=[('SHORT', 'pour une durée de 1 jour'), ('LONG', 'pour une durée de 1 an'), ('EUS_03_20', 'jusqu’à la fin de l’état d’urgence sanitaire ')], max_length=16, null=True, verbose_name='Durée')),
                        ('is_remote', models.BooleanField(default=False, verbose_name='Signé à distance ?')),
                        ('organisation', models.ForeignKey(default=aidants_connect.apps.mandats.models.get_staff_organisation_name_id, on_delete=django.db.models.deletion.PROTECT, related_name='mandats', to='aidants.organisation')),
                        ('usager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mandats', to='usagers.usager')),
                    ],
                    options={
                        'db_table': 'aidants_connect_web_mandat',
                    },
                ),
                migrations.CreateModel(
                    name='Connection',
                    fields=[
                        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                        ('state', models.TextField()),
                        ('nonce', models.TextField(default='No Nonce Provided')),
                        ('connection_type', models.CharField(choices=[('FS', 'FC as FS'), ('FI', 'FC as FI')], default='FI', max_length=2)),
                        ('demarches', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default='No démarche'), null=True, size=None)),
                        ('duree_keyword', models.CharField(choices=[('SHORT', 'pour une durée de 1 jour'), ('LONG', 'pour une durée de 1 an'), ('EUS_03_20', 'jusqu’à la fin de l’état d’urgence sanitaire ')], max_length=16, null=True)),
                        ('mandat_is_remote', models.BooleanField(default=False)),
                        ('expires_on', models.DateTimeField(default=aidants_connect.apps.mandats.models.default_connection_expiration_date)),
                        ('access_token', models.TextField(default='No token provided')),
                        ('code', models.TextField()),
                        ('demarche', models.TextField(default='No demarche provided')),
                        ('complete', models.BooleanField(default=False)),
                        ('aidant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='aidants.aidant')),
                        ('autorisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='mandats.autorisation')),
                        ('usager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='connections', to='usagers.usager')),
                    ],
                    options={
                        'verbose_name': 'connexion',
                        'db_table': 'aidants_connect_web_connection',
                    },
                ),
                migrations.AddField(
                    model_name='autorisation',
                    name='mandat',
                    field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='autorisations', to='mandats.mandat'),
                ),

            ]
        )
    ]
