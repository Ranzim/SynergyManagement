# Generated by Django 2.2 on 2021-02-19 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='message',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]
