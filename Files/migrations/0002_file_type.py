# Generated by Django 2.2.5 on 2019-09-09 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='type',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
    ]
