# Generated by Django 3.2.17 on 2023-03-28 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cardnumbers',
            fields=[
                ('cardnumber', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
