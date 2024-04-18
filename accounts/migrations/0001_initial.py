# Generated by Django 5.0.3 on 2024-04-18 22:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(blank=True, max_length=32, null=True, unique=True, verbose_name='Token')),
                ('token_type', models.CharField(blank=True, choices=[('su', 'SignUp token'), ('ce', 'Change email token'), ('pr', 'Password reset token')], max_length=2, null=True, verbose_name='Token type')),
                ('token_owner', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Token owner email')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Token creation date')),
                ('expired', models.BooleanField(default=False, verbose_name='Token expired')),
            ],
            options={
                'verbose_name': 'token',
                'verbose_name_plural': 'Tokens',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(blank=True, max_length=250, null=True, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('first_name', models.CharField(blank=True, max_length=125, null=True, verbose_name='First name')),
                ('surname', models.CharField(blank=True, max_length=125, null=True, verbose_name='Surname')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff status')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Superuser status')),
                ('is_active', models.BooleanField(default=True, verbose_name='User activated')),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='Last login')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date joined')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Store name')),
                ('store_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Store address')),
                ('store_city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Store city')),
                ('store_country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Store country')),
                ('store_phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Store phone number')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_info', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'store',
                'verbose_name_plural': 'stores',
            },
        ),
        migrations.CreateModel(
            name='UserBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='User balance')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='balance', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='UserShippingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shipping_info', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'shipping info',
                'verbose_name_plural': 'Shipping Infos',
            },
        ),
    ]
