# Generated by Django 5.1.2 on 2024-12-13 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_register_reg_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='reg_type',
            field=models.CharField(choices=[('Creator', 'Creator'), ('Viewer', 'Viewer')], max_length=10),
        ),
    ]
