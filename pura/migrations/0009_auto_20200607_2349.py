# Generated by Django 3.0.6 on 2020-06-07 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pura', '0008_auto_20200606_0237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('customer_id__id',)},
        ),
    ]
