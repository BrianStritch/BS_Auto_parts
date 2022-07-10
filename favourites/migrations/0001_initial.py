# Generated by Django 3.2 on 2022-06-19 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_alter_product_stock_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id',
                 models.BigAutoField(auto_created=True,
                                     primary_key=True,
                                     serialize=False,
                                     verbose_name='ID')),
                ('products',
                 models.ManyToManyField(blank=True, to='products.Product')),
                ('username',
                 models.OneToOneField(
                     on_delete=django.db.models.deletion.CASCADE,
                     to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Favourites',
            },
        ),
    ]
