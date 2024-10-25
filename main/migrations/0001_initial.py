
# Generated by Django 5.1.2 on 2024-10-23 18:08


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Makanan', 'Makanan'), ('Minuman', 'Minuman'), ('Camilan', 'Camilan')], max_length=20)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('restaurant_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ]
        ),
    ]