# Generated by Django 4.0.1 on 2022-01-23 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='api.deck'),
        ),
    ]
