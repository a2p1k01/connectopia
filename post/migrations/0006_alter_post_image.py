# Generated by Django 5.0 on 2023-12-30 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_remove_post_short_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='images/'),
        ),
    ]
