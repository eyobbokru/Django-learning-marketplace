# Generated by Django 5.0.1 on 2024-01-21 23:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0003_item_description_alter_item_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('name',), 'verbose_name_plural': 'Items'},
        ),
    ]
