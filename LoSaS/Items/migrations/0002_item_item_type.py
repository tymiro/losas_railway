# Generated by Django 4.2.4 on 2023-09-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('main hand', 'Main Hand'), ('off hand', 'Off Hand'), ('head', 'Head'), ('shoulder', 'Shoulder'), ('chest', 'Chest'), ('hands', 'Hands'), ('feet', 'Feet'), ('neck', 'Neck'), ('cape', 'Cape'), ('ring', 'Ring'), ('charm', 'Charm')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
