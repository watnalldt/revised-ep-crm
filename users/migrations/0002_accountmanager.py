# Generated by Django 4.2.8 on 2023-12-13 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountManager',
            fields=[
            ],
            options={
                'verbose_name': 'Account Manager',
                'verbose_name_plural': 'Account Managers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('users.user',),
        ),
    ]
