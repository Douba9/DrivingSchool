# Generated by Django 4.2.6 on 2023-10-18 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('h_total', models.IntegerField(default=0)),
                ('h_remaining', models.IntegerField(default=0)),
            ],
        ),
    ]
