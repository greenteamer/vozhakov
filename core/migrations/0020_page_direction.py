# Generated by Django 2.0 on 2018-01-13 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_direction'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='direction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Direction', verbose_name='Направление'),
        ),
    ]
