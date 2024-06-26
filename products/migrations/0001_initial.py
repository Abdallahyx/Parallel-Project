# Generated by Django 5.0.3 on 2024-04-24 06:51

import django.db.models.deletion
import mptt.fields
import products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Required and unique', max_length=255, unique=True, verbose_name='Category Name')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Category safe URL')),
                ('is_active', models.BooleanField(default=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/categories/', verbose_name='Photo')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Required', max_length=255, verbose_name='title')),
                ('slug', models.SlugField(max_length=255)),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/products/', verbose_name='Photo')),
                ('discount', models.IntegerField(default=0, verbose_name='Discount(Optional)')),
                ('is_active', models.BooleanField(default=True, help_text='Change product visibility', verbose_name='Product visibility')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2, verbose_name='Rating')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.category')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.store')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', help_text='Upload a product image', upload_to=products.models.upload_to, verbose_name='image')),
                ('is_featured', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_images', to='products.product')),
            ],
            options={
                'verbose_name': 'Product Image',
                'verbose_name_plural': 'Product Images',
            },
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('quantity_in_stock', models.PositiveIntegerField(default=0, verbose_name='Quantity in stock')),
                ('quantity_sold', models.PositiveIntegerField(default=0, verbose_name='Quantity sold')),
                ('stock_date', models.DateTimeField(blank=True, null=True, verbose_name='Stock date')),
                ('last_sales_date', models.DateTimeField(blank=True, null=True, verbose_name='Last sales date')),
                ('availability_status', models.IntegerField(choices=[(1, 'in stock'), (2, 'awaiting arrival'), (3, 'low in stock'), (4, 'out of stock')], default=4)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variations', to='products.product')),
            ],
            options={
                'unique_together': {('product', 'size')},
            },
        ),
    ]
