# Generated by Django 2.2.2 on 2019-06-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_site', '0002_auto_20190624_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='expire_date',
            field=models.DateField(),
        ),
    ]
