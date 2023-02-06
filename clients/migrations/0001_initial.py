# Generated by Django 4.1.5 on 2023-02-03 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('Premium', 'Premium'), ('Normal', 'Normal')], max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
