# Generated by Django 5.2 on 2025-07-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_web', '0008_alter_contact_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default='07:07:2025'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='time',
            field=models.TimeField(default='15:11:42'),
        ),
    ]
