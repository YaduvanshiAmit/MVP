# Generated by Django 3.0.8 on 2021-06-25 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mita', '0002_auto_20210625_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailentry',
            name='name',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
