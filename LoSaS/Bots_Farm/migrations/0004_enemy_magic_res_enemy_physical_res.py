# Generated by Django 4.2.4 on 2023-09-16 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bots_Farm', '0003_remove_enemy_armor_remove_enemy_magic_res'),
    ]

    operations = [
        migrations.AddField(
            model_name='enemy',
            name='magic_res',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='enemy',
            name='physical_res',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
