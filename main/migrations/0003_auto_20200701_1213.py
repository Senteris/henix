# Generated by Django 3.0.7 on 2020-07-01 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200701_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheat',
            name='oc_support',
            field=models.CharField(max_length=64, verbose_name='OC Support'),
        ),
        migrations.AlterField(
            model_name='cheat',
            name='price',
            field=models.FloatField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='cheat',
            name='status',
            field=models.CharField(choices=[('Detected', 'Detected'), ('Undetected', 'Undetected')], max_length=24, verbose_name='Status'),
        ),
    ]
