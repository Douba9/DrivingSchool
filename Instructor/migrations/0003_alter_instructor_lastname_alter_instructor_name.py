# Generated by Django 4.2.6 on 2023-11-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Instructor', '0002_instructor_lastname_instructor_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='lastname',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
    ]