# Generated by Django 5.0.6 on 2024-06-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t_donor',
            name='td_item',
            field=models.CharField(blank=True, choices=[('select', 'Select'), ('shoes', 'Shoes'), ('clothes', 'Clothes'), ('food items', 'Food Items')], max_length=50, null=True),
        ),
    ]
