# Generated by Django 3.0.7 on 2021-04-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='lamguage',
            field=models.CharField(default='exit', max_length=50),
            preserve_default=False,
        ),
    ]
