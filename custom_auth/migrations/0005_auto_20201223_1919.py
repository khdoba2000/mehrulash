# Generated by Django 3.1.4 on 2020-12-23 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0004_auto_20201223_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(help_text="telefon raqamingiz 7 ta raqam bo'lishi kerak", max_length=9, unique=True, validators=[django.core.validators.RegexValidator(message='Length has to be 9', regex='^.{9}$')]),
        ),
    ]
