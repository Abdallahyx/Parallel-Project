# Generated by Django 5.0.3 on 2024-04-24 06:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_item', models.IntegerField(default=0, verbose_name='Price per item')),
                ('quantity_in_stock', models.PositiveIntegerField(default=0, verbose_name='Quantity in stock')),
                ('quantity_sold', models.PositiveIntegerField(default=0, verbose_name='Quantity sold')),
                ('stock_date', models.DateTimeField(blank=True, null=True, verbose_name='Stock date')),
                ('last_sales_date', models.DateTimeField(blank=True, null=True, verbose_name='Last sales date')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_info', to='products.product', verbose_name='Product')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category', verbose_name='Product category')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stock_items', to='accounts.store', verbose_name='Store')),
            ],
            options={
                'verbose_name': 'stock item',
                'verbose_name_plural': 'Stock items',
            },
        ),
    ]
