# Generated by Django 2.1.5 on 2019-04-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20190409_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='review',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
