# Generated by Django 2.2.9 on 2020-01-25 18:47

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_registrationpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationpage',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True, null=True),
        ),
    ]
