# Generated by Django 4.1.7 on 2023-06-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookmark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_column='user_id', max_length=50)),
                ('place', models.CharField(db_column='place', max_length=50)),
            ],
            options={
                'db_table': 'bookmark',
            },
        ),
    ]
