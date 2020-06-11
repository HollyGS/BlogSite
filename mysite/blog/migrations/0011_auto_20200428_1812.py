# Generated by Django 3.0.5 on 2020-04-28 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200428_1309'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.AlterField(
            model_name='post',
            name='brief',
            field=models.CharField(default='...', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.CharField(default='', max_length=50),
        ),
    ]