# Generated by Django 3.2.4 on 2021-06-15 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0010_auto_20210615_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='client_name',
            field=models.CharField(default=None, max_length=20, verbose_name='Как в Вам обращаться?'),
        ),
    ]
