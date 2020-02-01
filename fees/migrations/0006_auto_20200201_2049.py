# Generated by Django 2.2.9 on 2020-02-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0005_accommodationfee_full_week_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodationfee',
            name='daily_fee',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
        ),
    ]