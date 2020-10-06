# Generated by Django 2.2.10 on 2020-10-05 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_geotag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geotag',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='file',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='geotag',
            name='type',
            field=models.CharField(blank=True, choices=[('point', 'Point'), ('line', 'Line'), ('polygon', 'Polygon')], max_length=20, null=True),
        ),
    ]
