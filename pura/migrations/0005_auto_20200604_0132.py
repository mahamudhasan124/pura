# Generated by Django 3.0.6 on 2020-06-03 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pura', '0004_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('customer_id',)},
        ),
    ]