# Generated by Django 5.1.2 on 2024-10-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='url_gambar',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
