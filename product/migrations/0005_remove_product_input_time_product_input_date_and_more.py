# Generated by Django 4.2 on 2023-04-09 09:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_input_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='input_time',
        ),
        migrations.AddField(
            model_name='product',
            name='input_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='입고'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='output_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='출고'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Inbound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_date', models.DateField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='product.product')),
            ],
        ),
    ]
