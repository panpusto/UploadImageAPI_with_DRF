# Generated by Django 4.1.7 on 2023-03-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
        ('accounts', '0002_accounttier_customuser_account_tier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounttier',
            name='thumbnail_size',
            field=models.ManyToManyField(blank=True, to='images.thumbnailsize'),
        ),
    ]
