# Generated by Django 3.1.4 on 2020-12-23 19:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='contact_info',
            field=models.CharField(default='https://t.me/', max_length=256, validators=[django.core.validators.MinLengthValidator(2, 'Contact info must be greater than 2 characters')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='phone_number',
            field=models.CharField(default=None, max_length=7, validators=[django.core.validators.MinLengthValidator(7, 'Phone number must be 7 characters')]),
        ),
    ]
