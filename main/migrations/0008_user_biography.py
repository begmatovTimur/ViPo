# Generated by Django 4.0.3 on 2022-06-17 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='biography',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
