# Generated by Django 3.1.4 on 2020-12-27 09:21

from django.db import migrations, models
import django.db.models.deletion
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20201227_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to=posts.models.get_upload_path)),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAlbum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='PostImage',
        ),
        migrations.AddField(
            model_name='image',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='posts.imagealbum'),
        ),
        migrations.AddField(
            model_name='post',
            name='album',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='posts.imagealbum'),
            preserve_default=False,
        ),
    ]
