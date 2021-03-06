# Generated by Django 3.2.9 on 2022-02-03 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_post_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cost',
            field=models.PositiveIntegerField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='barcode',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
