# Generated by Django 5.0.6 on 2024-06-28 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NameIntegrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название интеграции')),
            ],
        ),
        migrations.CreateModel(
            name='IntegrationsHook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hook', models.CharField(max_length=350, verbose_name='Хук для интеграции')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='integrations.nameintegrations')),
            ],
        ),
    ]
