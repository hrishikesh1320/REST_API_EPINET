# Generated by Django 4.2.5 on 2024-01-01 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='company',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('uwi', models.TextField()),
                ('data_type', models.IntegerField()),
                ('x', models.TextField()),
                ('y', models.TextField()),
                ('data_source_year', models.TextField()),
                ('created_on', models.TextField()),
                ('updated_on', models.TextField()),
            ],
        ),
    ]