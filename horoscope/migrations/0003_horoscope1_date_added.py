# Generated by Django 2.2.14 on 2020-07-26 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horoscope', '0002_auto_20200726_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='horoscope1',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
