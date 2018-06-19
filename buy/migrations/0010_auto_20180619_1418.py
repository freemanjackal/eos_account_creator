# Generated by Django 2.0.6 on 2018-06-19 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0009_stripecharge_price_cents'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripecharge',
            name='purchase',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buy.Purchase'),
        ),
        migrations.AddField(
            model_name='stripecharge',
            name='user_uuid',
            field=models.UUIDField(null=True),
        ),
    ]