# Generated by Django 3.0 on 2022-01-23 19:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='user',
            field=models.ManyToManyField(through='vehicule.Location', to=settings.AUTH_USER_MODEL),
        ),
    ]
