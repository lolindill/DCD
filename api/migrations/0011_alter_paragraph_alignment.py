# Generated by Django 4.2.16 on 2024-12-13 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_paragraph_remove_documentformat_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='alignment',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
