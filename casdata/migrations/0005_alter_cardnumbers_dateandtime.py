# Generated by Django 3.2.17 on 2023-03-28 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casdata', '0004_alter_cardnumbers_dateandtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardnumbers',
            name='dateandtime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
