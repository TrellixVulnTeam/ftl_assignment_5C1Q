# Generated by Django 2.2.7 on 2020-09-25 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0002_member_mid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='mid',
        ),
    ]
