# Generated by Django 3.2.4 on 2021-06-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_auto_20210615_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id_order',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Исполняется'), (2, 'Готов')], default=1, verbose_name='Статус заказа'),
        ),
    ]
