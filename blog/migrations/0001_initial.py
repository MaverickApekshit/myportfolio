# Generated by Django 2.2.6 on 2019-11-02 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=255)),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
