# Generated by Django 5.0.3 on 2024-04-26 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentinfo',
            name='payment_method',
            field=models.IntegerField(choices=[(1, 'By cash'), (2, 'By balance'), (3, 'By Paypal')], verbose_name='Payment method'),
        ),
    ]
