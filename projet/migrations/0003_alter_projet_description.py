# Generated by Django 4.0.1 on 2023-02-06 22:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0002_alter_projet_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]