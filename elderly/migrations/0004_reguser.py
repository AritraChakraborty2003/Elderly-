# Generated by Django 5.0 on 2024-03-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elderly', '0003_doctor_api_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('mobile', models.TextField()),
                ('location', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('patName', models.TextField()),
            ],
        ),
    ]
