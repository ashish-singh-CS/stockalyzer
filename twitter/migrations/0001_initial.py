# Generated by Django 3.0.5 on 2020-04-07 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PriceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yesterclose', models.DecimalField(decimal_places=2, max_digits=19)),
                ('first_mention', models.DecimalField(decimal_places=2, max_digits=19)),
                ('last_price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('last_volume', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('priceinfo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.PriceInfo')),
                ('ticker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Ticker')),
            ],
        ),
        migrations.CreateModel(
            name='NewsTrends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.News')),
                ('trends_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Trend')),
            ],
        ),
    ]
