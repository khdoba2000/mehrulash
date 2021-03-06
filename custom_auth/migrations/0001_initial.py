# Generated by Django 3.1.4 on 2020-12-23 11:56

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.IntegerField(help_text='telefon raqamingiz', unique=True, validators=[django.core.validators.RegexValidator(message='Length has to be 9', regex='^.{9}$')])),
                ('password', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(6, "Parol kamida 6 xonali bo'lishi kerak! ")])),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=16)),
                ('region', models.CharField(choices=[('Tashkent_city', 'Toshkent shahar'), ('Tashkent', 'Toshkent viloyat'), ('Nukus', 'Nukus'), ('Urgench', 'Urganch'), ('Bukhara', 'Buxoro'), ('Navoiy', 'Navoiy'), ('Termiz', 'Termiz'), ('Qarshi', 'Qarshi'), ('Samarkand', 'Samarqand'), ('Guliston', 'Guliston'), ('Djizzakh', 'Jizzax'), ('Fergana', "Farg'ona"), ('Namangan', 'Namangan'), ('Andijon', 'Andijon')], max_length=16)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
