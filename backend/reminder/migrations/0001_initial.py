# Generated by Django 2.0.2 on 2018-07-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval', models.IntegerField(default=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
