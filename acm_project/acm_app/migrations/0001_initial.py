# Generated by Django 4.1.7 on 2023-03-05 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScannedSupplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('logo_path', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('GRANTED', 'GRANTED'), ('REVOKED', 'REVOKED'), ('AMENDMENT', 'AMENDMENT'), ('NAME_CHANGE', 'NAME_CHANGE')], max_length=11)),
                ('new_supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='acm_app.supplier')),
                ('scanned_supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acm_app.scannedsupplier')),
            ],
        ),
    ]
