# Generated by Django 2.1.5 on 2020-02-28 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0002_auto_20200228_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline',
            field=models.DateTimeField(null=True),
        ),
    ]