# Generated by Django 5.1 on 2024-08-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_remove_usersession_temp_data_usersession_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('description', models.CharField(max_length=255)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='usersession',
            name='description',
        ),
        migrations.RemoveField(
            model_name='usersession',
            name='price',
        ),
        migrations.RemoveField(
            model_name='usersession',
            name='quantity',
        ),
        migrations.AddField(
            model_name='usersession',
            name='order_items',
            field=models.ManyToManyField(blank=True, to='bot.orderitem'),
        ),
    ]
