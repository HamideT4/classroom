# Generated by Django 4.1.6 on 2023-03-09 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClassroomApp', '0003_etudiant_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='genre',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=32),
        ),
    ]
