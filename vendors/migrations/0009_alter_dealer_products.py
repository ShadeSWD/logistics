# Generated by Django 5.0.1 on 2024-01-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0008_dealer_debt_alter_dealer_contractor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dealer',
            name='products',
            field=models.ManyToManyField(to='vendors.product', verbose_name='products'),
        ),
    ]
