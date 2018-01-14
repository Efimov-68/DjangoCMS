# Generated by Django 2.0.1 on 2018-01-14 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rabbitweb_ru', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
