# Generated by Django 3.0.5 on 2020-04-24 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0003_auto_20200424_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='priceinfo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.PriceInfo'),
        ),
    ]