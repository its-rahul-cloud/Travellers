# Generated by Django 4.1 on 2022-11-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='title',
            field=models.CharField(default='local', max_length=200),
        ),
    ]