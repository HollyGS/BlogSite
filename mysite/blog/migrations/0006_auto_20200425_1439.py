# Generated by Django 3.0.5 on 2020-04-25 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200425_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
