# Generated by Django 4.2.6 on 2023-11-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FertilizerPredictor', '0004_alter_data_chart_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='chart_type',
            field=models.CharField(choices=[('bar', 'bar'), ('line', 'line'), ('pie', 'pie')], default='bar', max_length=20),
        ),
    ]