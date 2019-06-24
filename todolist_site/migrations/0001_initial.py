# Generated by Django 2.2.2 on 2019-06-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('content', models.TextField()),
                ('expire_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('0', 'Pending'), ('1', 'Complete')], default='0', max_length=1)),
                ('priority', models.CharField(choices=[('3', 'High'), ('2', 'Medium'), ('1', 'Low')], default='1', max_length=1)),
            ],
        ),
    ]
