# Generated by Django 4.2 on 2025-02-16 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedpdf',
            name='processed',
        ),
        migrations.AddField(
            model_name='uploadedpdf',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='uploadedpdf',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pendiente'), ('PROCESSING', 'En proceso'), ('COMPLETE', 'Completado'), ('ERROR', 'Error')], default='PENDING', max_length=10),
        ),
        migrations.AlterField(
            model_name='uploadedpdf',
            name='pdf_file',
            field=models.FileField(upload_to='pdfs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])]),
        ),
    ]
