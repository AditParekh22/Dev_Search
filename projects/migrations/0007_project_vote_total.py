# Generated by Django 4.2.4 on 2023-08-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]