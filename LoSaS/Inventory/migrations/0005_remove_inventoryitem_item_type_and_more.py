# Generated by Django 4.2.4 on 2023-09-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0004_inventoryitem_item_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventoryitem',
            name='item_type',
        ),
        migrations.AddField(
            model_name='inventoryitem',
            name='category',
            field=models.CharField(choices=[('Main Hand', 'Main Hand'), ('Off Hand', 'Off Hand'), ('Head', 'Head'), ('Shoulder', 'Shoulder'), ('Chest', 'Chest'), ('Hands', 'Hands'), ('Feet', 'Feet'), ('Neck', 'Neck'), ('Cape', 'Cape'), ('Ring', 'Ring'), ('Charm', 'Charm')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
