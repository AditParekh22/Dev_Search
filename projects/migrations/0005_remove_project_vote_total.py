# Generated by Django 4.2.4 on 2023-08-21 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_featured_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='vote_total',
        ),
    ]