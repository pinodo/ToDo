# Generated by Django 4.1 on 2022-08-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_todolists_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolists',
            name='category',
            field=models.CharField(choices=[('Money', 'Money'), ('Language', 'Language'), ('Habit', 'Habit'), ('Job', 'Job'), ('Lifestyle', 'Life Style')], default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='todolists',
            name='priority',
            field=models.CharField(choices=[('IU', 'Important & Urgent'), ('INU', 'Important & Not Urgent'), ('NIU', 'Not Important & Urgent'), ('NINU', 'Not Important & Not Urgent')], default=1, max_length=4),
        ),
    ]
