# Generated by Django 3.1.7 on 2021-03-31 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='product',
        ),
    ]