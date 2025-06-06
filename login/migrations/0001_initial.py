# Generated by Django 5.1.7 on 2025-03-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(default='Unknown', max_length=100)),
                ('last_name', models.CharField(default='Unknown', max_length=100)),
                ('address', models.CharField(default='Unknown', max_length=200)),
                ('password', models.CharField(max_length=14)),
            ],
        ),
    ]
