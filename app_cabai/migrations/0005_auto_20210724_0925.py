# Generated by Django 3.2.5 on 2021-07-24 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cabai', '0004_jenispenyakit_solusi'),
    ]

    operations = [
        migrations.AddField(
            model_name='permasalahan',
            name='keterangan',
            field=models.CharField(default='Belum dilakukan diagnosis penyakit', max_length=100),
        ),
        migrations.AlterField(
            model_name='permasalahan',
            name='penjelasan',
            field=models.TextField(default='Belum dilakukan diagnosis penyakit'),
        ),
    ]