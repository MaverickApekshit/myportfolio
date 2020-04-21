# Generated by Django 2.2.6 on 2020-03-19 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20200312_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='projects.Project')),
            ],
        ),
    ]
