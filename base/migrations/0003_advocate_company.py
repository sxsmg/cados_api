# Generated by Django 4.1.3 on 2022-11-20 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.company'),
        ),
    ]
