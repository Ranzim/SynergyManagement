# Generated by Django 2.2 on 2021-02-19 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20210219_0515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='branch',
            field=models.CharField(max_length=56),
        ),
    ]
