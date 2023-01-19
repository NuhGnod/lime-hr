# Generated by Django 3.2.5 on 2023-01-18 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_code', models.CharField(default='CC', max_length=2)),
                ('upper_code', models.CharField(max_length=8)),
                ('lower_code', models.CharField(max_length=8)),
            ],
            options={
                'ordering': ['upper_code'],
            },
        ),
        migrations.CreateModel(
            name='CommonMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_code', models.CharField(default='CM', max_length=2)),
                ('upper_menu', models.CharField(max_length=8)),
                ('lower_menu', models.CharField(max_length=8)),
            ],
            options={
                'ordering': ['upper_menu'],
            },
        ),
    ]