# Generated by Django 2.2.6 on 2019-11-11 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='titile',
            new_name='title',
        ),
    ]