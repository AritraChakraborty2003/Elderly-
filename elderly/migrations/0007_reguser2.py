# Generated by Django 4.2.11 on 2024-04-23 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elderly', '0006_ambulance_book_delete_ambulance'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegUser2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('age', models.TextField()),
                ('medical_history', models.TextField()),
                ('bpm', models.EmailField(max_length=254)),
                ('sp_o2', models.TextField()),
                ('medicine', models.TextField()),
                ('condition', models.TextField()),
            ],
        ),
    ]