# Generated by Django 4.2 on 2023-04-21 17:41

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Generic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from=['name', 'play', 'position'], unique=True),
        ),
    ]
