# Generated by Django 4.2.9 on 2024-02-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0006_welcome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]