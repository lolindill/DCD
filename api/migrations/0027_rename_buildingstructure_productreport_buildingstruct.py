# Generated by Django 4.2.16 on 2025-02-18 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_alter_productreport_priority'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productreport',
            old_name='buildingStructure',
            new_name='buildingStruct',
        ),
    ]
