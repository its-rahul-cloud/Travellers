# Generated by Django 4.1 on 2022-11-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_bookedhouse_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
