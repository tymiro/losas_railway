# Generated by Django 4.2.4 on 2023-08-28 20:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Team', '0003_character_armor_character_constitution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]