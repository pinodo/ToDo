# Generated by Django 4.1 on 2022-08-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_todolists_category_alter_todolists_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolists',
            name='title',
            field=models.CharField(default='Untitled', max_length=200),
        ),
    ]
