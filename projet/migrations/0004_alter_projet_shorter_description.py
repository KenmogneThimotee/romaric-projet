# Generated by Django 4.0.1 on 2023-02-06 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet', '0003_alter_projet_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='shorter_description',
            field=models.CharField(max_length=45),
        ),
    ]
