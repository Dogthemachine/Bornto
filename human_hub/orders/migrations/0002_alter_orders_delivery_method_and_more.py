# Generated by Django 4.0.4 on 2022-06-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delivery_method',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='delivery_method'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='payment_method',
            field=models.CharField(blank=True, default='', max_length=70, verbose_name='payment_method'),
        ),
    ]
