# Generated by Django 3.0.7 on 2020-06-30 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('localusers', '0002_auto_20200630_1738'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchase',
            name='cheat',
        ),
        migrations.DeleteModel(
            name='Cheat',
        ),
        migrations.DeleteModel(
            name='Game',
        ),
        migrations.DeleteModel(
            name='Purchase',
        ),
    ]
