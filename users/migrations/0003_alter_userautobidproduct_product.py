# Generated by Django 3.2.5 on 2021-09-13 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210913_0837'),
        ('users', '0002_userbidconfig_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userautobidproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
