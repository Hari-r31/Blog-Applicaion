# Generated by Django 5.1.2 on 2024-12-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
