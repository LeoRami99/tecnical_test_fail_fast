# Generated by Django 5.1.2 on 2024-11-01 04:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BranchOffice',
            fields=[
                ('id_broff', models.BigAutoField(help_text='Identificador único para la sucursal.', primary_key=True, serialize=False, verbose_name='ID de Sucursal')),
                ('broff_name', models.CharField(help_text='Nombre descriptivo de la sucursal.', verbose_name='Nombre de Sucursal')),
                ('broff_code', models.CharField(help_text='Código único que identifica la sucursal dentro de la empresa.', verbose_name='Código de Sucursal')),
                ('broff_address', models.CharField(help_text='Dirección física de la sucursal.', verbose_name='Dirección')),
                ('broff_city', models.CharField(help_text='Ciudad donde está ubicada la sucursal.', verbose_name='Ciudad')),
                ('broff_state', models.CharField(help_text='Departamento o estado donde está ubicada la sucursal.', verbose_name='Departamento/Estado')),
                ('broff_country', models.CharField(help_text='País donde está ubicada la sucursal.', verbose_name='País')),
                ('broff_phone', models.CharField(help_text='Número de teléfono de la sucursal.', verbose_name='Teléfono')),
                ('broff_email', models.EmailField(help_text='Dirección de correo electrónico de la sucursal.', max_length=254, verbose_name='Correo Electrónico')),
                ('broff_active', models.BooleanField(default=True, help_text='Indica si la sucursal está activa (True) o inactiva (False).', verbose_name='Estado de la Sucursal')),
                ('company', models.ForeignKey(help_text='Compañía a la que pertenece esta sucursal.', on_delete=django.db.models.deletion.PROTECT, related_name='branch_offices', to='core.company', verbose_name='Compañía')),
            ],
            options={
                'verbose_name': 'Sucursal',
                'verbose_name_plural': 'Sucursales',
                'unique_together': {('company', 'broff_code')},
            },
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id_cosce', models.BigAutoField(help_text='Identificador único para el centro de costo.', primary_key=True, serialize=False, verbose_name='ID del Centro de Costo')),
                ('cosce_code', models.CharField(help_text='Código único que identifica el centro de costo.', verbose_name='Código')),
                ('cosce_name', models.CharField(help_text='Nombre descriptivo del centro de costo.', verbose_name='Nombre')),
                ('cosce_description', models.TextField(blank=True, help_text='Descripción detallada del centro de costo y su propósito.', verbose_name='Descripción')),
                ('cosce_budget', models.DecimalField(decimal_places=2, default=0, help_text='Presupuesto asignado al centro de costo.', max_digits=15, verbose_name='Presupuesto')),
                ('cosce_level', models.PositiveSmallIntegerField(default=1, help_text='Nivel en la jerarquía de centros de costo (1 para nivel superior).', verbose_name='Nivel Jerárquico')),
                ('cosce_active', models.BooleanField(default=True, help_text='Indica si el centro de costo está activo (True) o inactivo (False).', verbose_name='Estado del Centro de Costo')),
                ('company', models.ForeignKey(help_text='Compañía a la que pertenece este centro de costo.', on_delete=django.db.models.deletion.PROTECT, related_name='cost_centers', to='core.company', verbose_name='Compañía')),
                ('cosce_parent', models.ForeignKey(blank=True, help_text='Centro de costo superior en la jerarquía organizacional.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='ERP.costcenter', verbose_name='Centro de Costo Padre')),
            ],
            options={
                'verbose_name': 'Centro de Costo',
                'verbose_name_plural': 'Centros de Costo',
                'unique_together': {('company', 'cosce_code')},
            },
        ),
    ]