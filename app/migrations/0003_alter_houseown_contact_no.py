# Generated by Django 4.1 on 2022-11-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_house_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseown',
            name='contact_no',
            field=models.IntegerField(default=1, max_length=10),
        ),
    ]
