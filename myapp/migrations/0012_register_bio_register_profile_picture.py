# Generated by Django 5.1.2 on 2024-12-15 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_rename_author_blogs_author_id_blogs_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]
