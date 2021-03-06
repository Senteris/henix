# Generated by Django 3.0.7 on 2020-07-01 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
        ),
        migrations.RemoveField(
            model_name='cheat',
            name='last_detect_at',
        ),
        migrations.AddField(
            model_name='cheat',
            name='mini_description',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Mini description'),
        ),
        migrations.AddField(
            model_name='cheat',
            name='oc_support',
            field=models.CharField(default='Windows 7, 8.1, 10', max_length=64, verbose_name='OC Support'),
        ),
        migrations.AddField(
            model_name='cheat',
            name='price',
            field=models.FloatField(default=159, verbose_name='Price'),
        ),
        migrations.AddField(
            model_name='cheat',
            name='status',
            field=models.CharField(choices=[('Detected', 'Detected'), ('Undetected', 'Undetected')], default='Undetected', max_length=24, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment_id',
            field=models.CharField(max_length=64, verbose_name='Payment id'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(choices=[('Unpaid', 'Unpaid'), ('Pending', 'Pending'), ('Paid', 'Paid')], max_length=24, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, verbose_name='Key')),
                ('is_sold', models.BooleanField(blank=True, default=False, verbose_name='Is sold')),
                ('cheat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cheat', verbose_name='Cheat')),
            ],
        ),
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=24, verbose_name='Title')),
                ('last_hit', models.DateTimeField(blank=True, null=True, verbose_name='Last hit')),
                ('cheat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cheat', verbose_name='Cheat')),
            ],
        ),
        migrations.CreateModel(
            name='CheatFunction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='The best function', verbose_name='Description')),
                ('cheat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Cheat', verbose_name='Cheat')),
            ],
        ),
    ]
