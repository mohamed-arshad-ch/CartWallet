# Generated by Django 3.1.3 on 2020-11-15 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managewallet', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='managewallet.customeuser'),
            preserve_default=False,
        ),
    ]
