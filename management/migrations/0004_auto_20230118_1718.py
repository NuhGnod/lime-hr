# Generated by Django 3.2.5 on 2023-01-18 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_cc2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cc2',
            name='id',
        ),
        migrations.AlterField(
            model_name='cc2',
            name='common_code',
            field=models.CharField(default='', max_length=8, primary_key=True, serialize=False),
        ),
    ]
