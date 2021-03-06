# Generated by Django 3.1.7 on 2021-04-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20210412_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=254)),
                ('title', models.CharField(max_length=254)),
                ('image', models.ImageField(upload_to='user_images')),
                ('upload_image_file_path', models.CharField(default='not found', max_length=254)),
                ('comments', models.TextField()),
            ],
        ),
    ]
