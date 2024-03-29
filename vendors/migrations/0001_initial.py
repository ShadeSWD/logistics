# Generated by Django 5.0.1 on 2024-01-25 12:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='change date')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('country', models.CharField(max_length=60, verbose_name='country')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('street', models.CharField(max_length=100, verbose_name='street')),
                ('house', models.IntegerField(verbose_name='house number')),
                ('building', models.IntegerField(blank=True, null=True, verbose_name='building number')),
                ('letter', models.CharField(max_length=5, verbose_name='building letter')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='change date')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('model', models.CharField(max_length=100, verbose_name='model')),
                ('release_date', models.DateField(verbose_name='release date')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
        ),
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='change date')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendors.contacts')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='owner')),
                ('products', models.ManyToManyField(to='vendors.product')),
            ],
        ),
    ]
