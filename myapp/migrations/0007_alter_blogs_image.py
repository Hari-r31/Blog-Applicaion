# Generated by Django 5.1.2 on 2024-12-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_blogs_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(null=True, upload_to='media/img/'),
        ),
    ]
