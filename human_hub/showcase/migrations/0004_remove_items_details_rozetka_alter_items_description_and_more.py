# Generated by Django 4.0.4 on 2022-06-14 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_alter_balance_options_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='details_rozetka',
        ),
        migrations.AlterField(
            model_name='items',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='how it fits'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description_en',
            field=models.TextField(blank=True, default='', null=True, verbose_name='how it fits'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description_ru',
            field=models.TextField(blank=True, default='', null=True, verbose_name='how it fits'),
        ),
        migrations.AlterField(
            model_name='items',
            name='description_uk',
            field=models.TextField(blank=True, default='', null=True, verbose_name='how it fits'),
        ),
    ]