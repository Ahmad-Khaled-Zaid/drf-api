# Generated by Django 4.1 on 2022-08-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='reservation_by',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]