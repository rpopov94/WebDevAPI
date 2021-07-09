# Generated by Django 3.2.5 on 2021-07-04 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('geo', models.CharField(max_length=255)),
                ('parks', models.IntegerField()),
                ('stores', models.IntegerField()),
                ('schools', models.IntegerField()),
                ('kindergartens', models.IntegerField()),
            ],
        ),
    ]
