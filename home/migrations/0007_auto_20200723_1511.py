# Generated by Django 2.2.14 on 2020-07-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200723_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webusers',
            name='city',
        ),
        migrations.RemoveField(
            model_name='webusers',
            name='country',
        ),
        migrations.RemoveField(
            model_name='webusers',
            name='state',
        ),
        migrations.AddField(
            model_name='webusers',
            name='location',
            field=models.CharField(blank=True, max_length=50, verbose_name='kalanki'),
        ),
    ]
