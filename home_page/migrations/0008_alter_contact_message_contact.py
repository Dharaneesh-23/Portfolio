# Generated by Django 4.2.9 on 2024-02-01 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_contact_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_message',
            name='contact',
            field=models.CharField(max_length=200),
        ),
    ]
