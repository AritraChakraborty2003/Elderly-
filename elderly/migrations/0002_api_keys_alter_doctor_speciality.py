# Generated by Django 5.0 on 2024-03-24 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elderly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='api_keys',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('uname', models.TextField()),
                ('api_key', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(max_length=100),
        ),
    ]
