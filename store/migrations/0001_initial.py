# Generated by Django 4.2 on 2025-02-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('product_name', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('product_code', models.CharField(blank=True, max_length=255, null=True)),
                ('processor', models.CharField(blank=True, max_length=255, null=True)),
                ('graphics', models.CharField(blank=True, max_length=255, null=True)),
                ('hard_disk', models.CharField(blank=True, max_length=255, null=True)),
                ('ram', models.CharField(blank=True, max_length=255, null=True)),
                ('screen', models.CharField(blank=True, max_length=255, null=True)),
                ('battery', models.CharField(blank=True, max_length=255, null=True)),
                ('warranty', models.CharField(blank=True, max_length=255, null=True)),
                ('so_software', models.CharField(blank=True, max_length=255, null=True)),
                ('general', models.TextField(blank=True, null=True)),
                ('connections', models.CharField(blank=True, max_length=255, null=True)),
                ('audio', models.CharField(blank=True, max_length=255, null=True)),
                ('webcam', models.CharField(blank=True, max_length=255, null=True)),
                ('certifications', models.CharField(blank=True, max_length=255, null=True)),
                ('packing_size', models.CharField(blank=True, max_length=255, null=True)),
                ('memory_reader', models.CharField(blank=True, max_length=255, null=True)),
                ('keyboard', models.CharField(blank=True, max_length=255, null=True)),
                ('optical_driver', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
