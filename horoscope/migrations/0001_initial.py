# Generated by Django 2.2.14 on 2020-07-26 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='horoscope1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Mesh', models.TextField(null=True)),
                ('Brish', models.TextField(null=True)),
                ('Mithun', models.TextField(null=True)),
                ('Karkat', models.TextField(null=True)),
                ('Singha', models.TextField(null=True)),
                ('Kanya', models.TextField(null=True)),
                ('Tula', models.TextField(null=True)),
                ('Brischik', models.TextField(null=True)),
                ('Dhan', models.TextField(null=True)),
                ('Makar', models.TextField(null=True)),
                ('Kumbha', models.TextField(null=True)),
                ('Min', models.TextField(null=True)),
            ],
        ),
    ]
