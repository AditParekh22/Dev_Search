# Generated by Django 4.2.4 on 2023-09-15 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_review_owner_alter_review_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total', 'title']},
        ),
    ]
