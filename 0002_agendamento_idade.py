# Generated by Django 5.1.4 on 2024-12-10 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psicologos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agendamento',
            name='idade',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
