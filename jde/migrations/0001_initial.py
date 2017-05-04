# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-03 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='F0101',
            fields=[
                ('clave', models.IntegerField(db_column='ABAN8', primary_key=True, serialize=False)),
                ('nombre', models.CharField(db_column='ABALPH', max_length=40)),
                ('tipo', models.CharField(db_column='ABAT1', max_length=3)),
                ('rfc', models.CharField(db_column='ABTAX', max_length=20)),
            ],
            options={
                'db_table': '"CRPDTA"."F0101"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='F5903000',
            fields=[
                ('ftgenkey', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('fttax', models.CharField(blank=True, max_length=20, null=True)),
                ('fttaxs', models.CharField(blank=True, max_length=20, null=True)),
                ('ftbrtpo', models.CharField(max_length=3)),
                ('fttxr1', models.IntegerField(default=0)),
                ('fttxr2', models.IntegerField(default=0)),
                ('fttxr3', models.IntegerField(default=0)),
                ('fttxr4', models.IntegerField(default=0)),
                ('fttxr5', models.IntegerField(default=0)),
                ('ftafa1', models.IntegerField(default=0)),
                ('ftafa2', models.IntegerField(default=0)),
                ('ftafa3', models.IntegerField(default=0)),
                ('ftafa4', models.IntegerField(default=0)),
                ('ftafa5', models.IntegerField(default=0)),
                ('ftcrcd', models.CharField(blank=True, max_length=3, null=True)),
                ('ftcrr', models.IntegerField(default=0)),
                ('ftamrt1', models.IntegerField(default=0)),
                ('ftamrt2', models.IntegerField(default=0)),
                ('ftamrt3', models.IntegerField(default=0)),
                ('ftlo01', models.CharField(blank=True, max_length=5, null=True)),
                ('fturab', models.IntegerField(default=0)),
                ('fturat', models.IntegerField(default=0)),
                ('fturcd', models.CharField(blank=True, max_length=2, null=True)),
                ('fturdt', models.IntegerField(default=0)),
                ('fturrf', models.CharField(blank=True, max_length=15, null=True)),
                ('ftuser', models.CharField(blank=True, max_length=10, null=True)),
                ('ftpid', models.CharField(blank=True, max_length=10, null=True)),
                ('ftjobn', models.CharField(blank=True, max_length=10, null=True)),
                ('ftupmj', models.IntegerField(default=0)),
                ('ftupmt', models.IntegerField(default=0)),
                ('ftivd', models.IntegerField(default=0)),
                ('ftan8', models.IntegerField(default=0)),
            ],
            options={
                'db_table': '"CRPDTA"."F5903000"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_AUTORIZACIONES',
            fields=[
                ('orden', models.IntegerField()),
                ('ruta', models.CharField(max_length=12)),
                ('estado', models.CharField(max_length=2)),
                ('un', models.CharField(max_length=12)),
                ('oc_compania', models.CharField(max_length=5)),
                ('oc_tipo', models.CharField(max_length=2)),
                ('oc', models.IntegerField(primary_key=True, serialize=False)),
                ('oc_sufix', models.CharField(max_length=3)),
                ('autorizador', models.IntegerField()),
                ('autorizador_desc', models.CharField(max_length=40)),
                ('autorizacion_fecha', models.DateField()),
                ('autorizacion_hora', models.IntegerField()),
                ('lista_estados', models.CharField(max_length=4000)),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_AUTORIZACIONES"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_COMPANIAS',
            fields=[
                ('comp_code', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('comp_desc', models.CharField(max_length=30)),
                ('comp_book_code', models.IntegerField()),
                ('book_desc', models.CharField(max_length=80)),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_COMPANIAS"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_INVENTARIO',
            fields=[
                ('proyecto_cve', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('proyecto_desc', models.CharField(max_length=30)),
                ('articulo_cve', models.CharField(max_length=25)),
                ('articulo_desc', models.CharField(max_length=60)),
                ('imglpt', models.CharField(max_length=4)),
                ('un_cve', models.CharField(max_length=12)),
                ('un_desc', models.CharField(max_length=40)),
                ('fecha_recepcion', models.DateField()),
                ('cantidad_recep', models.DecimalField(decimal_places=4, max_digits=20)),
                ('costounimin', models.DecimalField(decimal_places=4, max_digits=20)),
                ('costouniavg', models.DecimalField(decimal_places=4, max_digits=20)),
                ('costounimax', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_INVENTARIO"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_INVENTARIO_UN',
            fields=[
                ('proyecto_cve', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('proyecto_desc', models.CharField(max_length=30)),
                ('cantidad_recep', models.DecimalField(decimal_places=4, max_digits=20)),
                ('costounimin', models.DecimalField(decimal_places=4, max_digits=20)),
                ('costouniavg', models.DecimalField(decimal_places=4, max_digits=20)),
                ('costounimax', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_INVENTARIOUN"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_RECEPCIONES',
            fields=[
                ('fecha_lm', models.DateField()),
                ('cantidad_recib', models.IntegerField()),
                ('udm_recib', models.CharField(max_length=2)),
                ('pu_ex', models.IntegerField()),
                ('monto_recib_ex', models.IntegerField()),
                ('moneda', models.CharField(max_length=3)),
                ('tasa', models.IntegerField()),
                ('pu_mx', models.IntegerField()),
                ('monto_recib_mx', models.IntegerField()),
                ('impuesto', models.CharField(max_length=10)),
                ('impuesto_flag', models.CharField(max_length=1)),
                ('batch', models.IntegerField()),
                ('batch_tipo', models.CharField(max_length=2)),
                ('activo', models.CharField(max_length=25)),
                ('ubicacion', models.CharField(max_length=20)),
                ('lote', models.CharField(max_length=30)),
                ('contenedor', models.CharField(max_length=20)),
                ('observaciones', models.CharField(max_length=30)),
                ('updater', models.CharField(max_length=10)),
                ('updater_desc', models.CharField(max_length=40)),
                ('fecha_update', models.DateField()),
                ('oc_compania', models.CharField(max_length=5)),
                ('oc_tipo', models.CharField(max_length=2)),
                ('oc', models.IntegerField(primary_key=True, serialize=False)),
                ('oc_linea', models.IntegerField()),
                ('oc_linea_tipo', models.CharField(max_length=2)),
                ('oc_sufix', models.CharField(max_length=3)),
                ('tran_compania', models.CharField(max_length=5)),
                ('tran_un', models.CharField(max_length=12)),
                ('tran_tipo', models.CharField(max_length=1)),
                ('tran_tipo_desc', models.CharField(max_length=19)),
                ('tran_linea', models.IntegerField()),
                ('doc_compania', models.CharField(max_length=5)),
                ('doc_tipo', models.CharField(max_length=2)),
                ('doc', models.IntegerField()),
                ('doc_linea', models.IntegerField()),
                ('doc_je_linea', models.IntegerField()),
                ('doc_factura', models.CharField(max_length=25)),
                ('proveedor', models.IntegerField()),
                ('item', models.IntegerField()),
                ('item_numero', models.CharField(max_length=25)),
                ('item_descripcion', models.CharField(max_length=60)),
                ('item_glclass', models.CharField(max_length=4)),
                ('originador', models.CharField(max_length=10)),
                ('originador_desc', models.CharField(max_length=40)),
                ('fecha_creacion', models.DateField()),
                ('fecha_tran', models.DateField()),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_RECEPCIONES"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_RECEPSINCOTEJO',
            fields=[
                ('oc_compania', models.CharField(max_length=5)),
                ('oc_compania_desc', models.CharField(max_length=30)),
                ('oc_proyecto', models.CharField(max_length=3)),
                ('oc_proyecto_desc', models.CharField(max_length=30)),
                ('oc_un', models.CharField(max_length=12)),
                ('oc_un_desc', models.CharField(max_length=60)),
                ('oc_numero', models.IntegerField(primary_key=True, serialize=False)),
                ('oc_tipo', models.CharField(max_length=2)),
                ('oc_tipo_desc', models.CharField(max_length=30)),
                ('oc_linea', models.IntegerField()),
                ('oc_linea_tipo', models.CharField(max_length=2)),
                ('oc_linea_tipo_desc', models.CharField(max_length=30)),
                ('oc_fecha_creacion', models.DateField()),
                ('oc_fecha_cancelacion', models.DateField()),
                ('oc_estado_ultimo', models.CharField(max_length=3)),
                ('oc_estado_siguiente', models.CharField(max_length=3)),
                ('oc_comprador', models.IntegerField()),
                ('oc_comprador_desc', models.CharField(max_length=40)),
                ('oc_originador', models.CharField(max_length=10)),
                ('oc_originador_desc', models.CharField(max_length=40)),
                ('oc_proveedor', models.IntegerField()),
                ('oc_proveedor_desc', models.CharField(max_length=40)),
                ('oc_item', models.IntegerField()),
                ('oc_item_numero', models.CharField(max_length=25)),
                ('oc_item_desc', models.CharField(max_length=60)),
                ('oc_cantidad_solic', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_udm', models.CharField(max_length=2)),
                ('oc_udm_desc', models.CharField(max_length=30)),
                ('oc_cantidad_recib', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_cantidad_xrecib', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_recepcion', models.CharField(max_length=9)),
                ('oc_pu_ex', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_total_ex', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_monto_recib_ex', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_monto_xrecib_ex', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_moneda', models.CharField(max_length=3)),
                ('oc_tasa', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_pu_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_total_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_monto_recib_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('oc_monto_xrecib_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_no', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_compania', models.CharField(max_length=5)),
                ('recepcion_tipo', models.CharField(max_length=2)),
                ('recepcion_doc', models.IntegerField()),
                ('recepcion_linea', models.IntegerField()),
                ('recepcion_fecha', models.DateField()),
                ('recepcion_fecha_lm', models.DateField()),
                ('recepcion_cantidad', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_udm', models.CharField(max_length=2)),
                ('recepcion_pu_ex', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_monto_ex', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_moneda', models.CharField(max_length=3)),
                ('recepcion_tasa', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_pu_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_monto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('recepcion_contenedor', models.CharField(max_length=20)),
                ('recepcion_batch', models.IntegerField()),
                ('recepcion_batch_tipo', models.CharField(max_length=2)),
                ('recepcion_originador', models.CharField(max_length=10)),
                ('recepcion_originador_desc', models.CharField(max_length=40)),
                ('fac_compania', models.CharField(max_length=5)),
                ('fac_tipo', models.CharField(max_length=2)),
                ('fac', models.IntegerField()),
                ('fac_linea', models.IntegerField()),
                ('fac_updater', models.CharField(max_length=10)),
                ('fac_updater_desc', models.CharField(max_length=40)),
                ('fac_fecha_update', models.DateField()),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_RECEPSINCOTEJO"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_SCOMPRAS',
            fields=[
                ('req_compania', models.CharField(max_length=5)),
                ('req_compania_desc', models.CharField(max_length=30)),
                ('req_un', models.CharField(max_length=12)),
                ('req_un_desc', models.CharField(max_length=60)),
                ('req_un_proyecto', models.CharField(max_length=3)),
                ('req_un_proyecto_desc', models.CharField(max_length=30)),
                ('req_tipo', models.CharField(max_length=2)),
                ('req_tipo_desc', models.CharField(max_length=30)),
                ('req', models.IntegerField(primary_key=True, serialize=False)),
                ('req_linea', models.IntegerField()),
                ('req_linea_tipo', models.CharField(max_length=2)),
                ('req_generador', models.CharField(max_length=10)),
                ('req_generador_desc', models.CharField(max_length=40)),
                ('req_fecha_creacion', models.DateTimeField()),
                ('req_fecha_necesidad', models.DateTimeField()),
                ('req_estado_last', models.CharField(max_length=3)),
                ('req_estado_last_desc', models.CharField(max_length=30)),
                ('req_estado_next', models.CharField(max_length=3)),
                ('req_item_numero', models.CharField(max_length=25)),
                ('req_item_desc', models.CharField(max_length=61)),
                ('req_comprador', models.IntegerField()),
                ('req_comprador_desc', models.CharField(max_length=40)),
                ('req_cantidad_solicitada', models.CharField(max_length=30)),
                ('req_udm', models.CharField(max_length=2)),
                ('req_udm_desc', models.CharField(max_length=30)),
                ('cot_compania', models.CharField(max_length=5)),
                ('cot_tipo', models.CharField(max_length=2)),
                ('cot', models.IntegerField()),
                ('cot_linea', models.IntegerField()),
                ('cot_generador', models.CharField(max_length=10)),
                ('cot_fecha_creacion', models.DateTimeField()),
                ('cot_estado_last', models.CharField(max_length=3)),
                ('cot_estado_last_desc', models.CharField(max_length=30)),
                ('cot_estado_next', models.CharField(max_length=3)),
                ('ord_compania', models.CharField(max_length=5)),
                ('ord_tipo', models.CharField(max_length=2)),
                ('ord_tipo_desc', models.CharField(max_length=30)),
                ('ord', models.IntegerField()),
                ('ord_fecha_creacion', models.DateTimeField()),
                ('ord_fecha_entrega', models.DateTimeField()),
                ('ord_generador', models.CharField(max_length=10)),
                ('ord_generador_desc', models.CharField(max_length=40)),
                ('ord_linea', models.IntegerField()),
                ('ord_proveedor', models.IntegerField()),
                ('ord_proveedor_desc', models.CharField(max_length=40)),
                ('ord_estado_last', models.CharField(max_length=3)),
                ('ord_estado_last_desc', models.CharField(max_length=30)),
                ('ord_estado_next', models.CharField(max_length=3)),
                ('ord_cantidad_solic', models.IntegerField()),
                ('ord_udm', models.CharField(max_length=2)),
                ('ord_udm_desc', models.CharField(max_length=30)),
                ('ord_cantidad_recib', models.CharField(max_length=30)),
                ('ord_cantidad_xrecib', models.CharField(max_length=30)),
                ('ord_recepcion', models.CharField(max_length=9)),
                ('ord_pu_ex', models.CharField(max_length=30)),
                ('ord_total_ex', models.CharField(max_length=30)),
                ('ord_monto_recib_ex', models.CharField(max_length=30)),
                ('ord_monto_xrecib_ex', models.CharField(max_length=30)),
                ('ord_moneda', models.CharField(max_length=3)),
                ('ord_moneda_desc', models.CharField(max_length=30)),
                ('ord_tasa', models.CharField(max_length=30)),
                ('ord_pu_mx', models.CharField(max_length=30)),
                ('ord_total_mx', models.CharField(max_length=30)),
                ('ord_monto_recib_mx', models.CharField(max_length=30)),
                ('ord_monto_xrecib_mx', models.CharField(max_length=30)),
                ('ord_impuesto', models.CharField(max_length=10)),
                ('ord_impuesto_desc', models.CharField(max_length=30)),
                ('ord_impuesto_flag', models.CharField(max_length=2)),
                ('ord_descuento', models.IntegerField()),
                ('ord_termino_pago', models.CharField(max_length=3)),
                ('ord_termino_pago_desc', models.CharField(max_length=30)),
                ('ord_updated_by', models.CharField(max_length=10)),
                ('ord_updated_by_desc', models.CharField(max_length=40)),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_SCOMPRAS"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VIEW_UNIDADES',
            fields=[
                ('clave', models.CharField(db_column='CLAVE', max_length=12, primary_key=True, serialize=False)),
                ('tipo', models.CharField(db_column='TIPO', max_length=2)),
                ('compania', models.CharField(db_column='COMPANIA', max_length=5)),
                ('desc_corta', models.CharField(db_column='DESC_CORTA', max_length=30)),
                ('desc_larga', models.CharField(db_column='DESC_LARGA', max_length=75)),
                ('reclass', models.CharField(db_column='RECLASS', max_length=10)),
            ],
            options={
                'db_table': '"NUVPD"."VIEW_UNIDADES"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VM_PORF_COMPRAS',
            fields=[
                ('base', models.CharField(max_length=30)),
                ('doc_compania', models.CharField(max_length=5)),
                ('doc_compania_desc', models.CharField(max_length=30)),
                ('anio', models.CharField(max_length=4)),
                ('periodo', models.CharField(max_length=2)),
                ('doc_tipo', models.CharField(max_length=2)),
                ('doc_tipo_desc', models.CharField(max_length=30)),
                ('doc_numero', models.IntegerField(primary_key=True, serialize=False)),
                ('doc_fecha_lm', models.DateField()),
                ('un_proyecto', models.CharField(max_length=3)),
                ('un_proyecto_desc', models.CharField(max_length=30)),
                ('un_proyecto_zona', models.CharField(max_length=30)),
                ('un_proyecto_tipo', models.CharField(max_length=2)),
                ('un_proyecto_tipo_desc', models.CharField(max_length=60)),
                ('un', models.CharField(max_length=12)),
                ('un_desc', models.CharField(max_length=60)),
                ('cuenta_objeto', models.CharField(max_length=6)),
                ('cuenta_auxiliar', models.CharField(max_length=8)),
                ('cuenta_desc', models.CharField(max_length=30)),
                ('cuenta_tipo', models.CharField(max_length=3)),
                ('cuenta_tipo_desc', models.CharField(max_length=30)),
                ('cuenta_clase', models.CharField(max_length=3)),
                ('cuenta_clase_desc', models.CharField(max_length=30)),
                ('cuenta_flujo', models.CharField(max_length=3)),
                ('cuenta_flujo_desc', models.CharField(max_length=30)),
                ('cuenta_clase_porf', models.CharField(max_length=3)),
                ('cuenta_clase_porf_desc', models.CharField(max_length=30)),
                ('monto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('enero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('febrero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('marzo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('abril_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('mayo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('junio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('julio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('agosto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('septiembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('octubre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('noviembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('diciembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': '"NUVPD"."VM_PORF_COMPRAS"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VM_PORF_CXC',
            fields=[
                ('base', models.CharField(max_length=30)),
                ('doc_compania', models.CharField(max_length=5)),
                ('doc_compania_desc', models.CharField(max_length=30)),
                ('anio', models.CharField(max_length=4)),
                ('periodo', models.CharField(max_length=2)),
                ('doc_tipo', models.CharField(max_length=2)),
                ('doc_tipo_desc', models.CharField(max_length=30)),
                ('doc_numero', models.IntegerField(primary_key=True, serialize=False)),
                ('doc_fecha_lm', models.DateField()),
                ('un_proyecto', models.CharField(max_length=3)),
                ('un_proyecto_desc', models.CharField(max_length=30)),
                ('un_proyecto_zona', models.CharField(max_length=30)),
                ('un_proyecto_tipo', models.CharField(max_length=2)),
                ('un_proyecto_tipo_desc', models.CharField(max_length=60)),
                ('un', models.CharField(max_length=12)),
                ('un_desc', models.CharField(max_length=60)),
                ('cuenta_numero', models.CharField(max_length=29)),
                ('cuenta_desc', models.CharField(max_length=30)),
                ('cuenta_tipo', models.CharField(max_length=3)),
                ('cuenta_tipo_desc', models.CharField(max_length=30)),
                ('cuenta_clase', models.CharField(max_length=3)),
                ('cuenta_clase_desc', models.CharField(max_length=30)),
                ('cuenta_flujo', models.CharField(max_length=3)),
                ('cuenta_flujo_desc', models.CharField(max_length=30)),
                ('cuenta_porf_clase', models.CharField(max_length=3)),
                ('cuenta_porf_clase_desc', models.CharField(max_length=30)),
                ('monto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('enero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('febrero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('marzo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('abril_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('mayo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('junio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('julio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('agosto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('septiembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('octubre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('noviembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('diciembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': '"NUVPD"."VM_PORF_CXC"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VM_PORF_CXP',
            fields=[
                ('base', models.CharField(max_length=30)),
                ('doc_compania', models.CharField(max_length=5)),
                ('doc_compania_desc', models.CharField(max_length=30)),
                ('anio', models.CharField(max_length=4)),
                ('periodo', models.CharField(max_length=2)),
                ('doc_tipo', models.CharField(max_length=2)),
                ('doc_tipo_desc', models.CharField(max_length=30)),
                ('doc_numero', models.IntegerField(primary_key=True, serialize=False)),
                ('doc_fecha_lm', models.DateField()),
                ('un_proyecto', models.CharField(max_length=3)),
                ('un_proyecto_desc', models.CharField(max_length=30)),
                ('un_proyecto_zona', models.CharField(max_length=30)),
                ('un_proyecto_tipo', models.CharField(max_length=2)),
                ('un_proyecto_tipo_desc', models.CharField(max_length=60)),
                ('un', models.CharField(max_length=12)),
                ('un_desc', models.CharField(max_length=60)),
                ('cuenta_numero', models.CharField(max_length=29)),
                ('cuenta_desc', models.CharField(max_length=30)),
                ('cuenta_tipo', models.CharField(max_length=3)),
                ('cuenta_tipo_desc', models.CharField(max_length=30)),
                ('cuenta_clase', models.CharField(max_length=3)),
                ('cuenta_clase_desc', models.CharField(max_length=30)),
                ('cuenta_flujo', models.CharField(max_length=3)),
                ('cuenta_flujo_desc', models.CharField(max_length=30)),
                ('cuenta_porf_clase', models.CharField(max_length=3)),
                ('cuenta_porf_clase_desc', models.CharField(max_length=30)),
                ('monto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('enero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('febrero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('marzo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('abril_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('mayo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('junio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('julio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('agosto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('septiembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('octubre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('noviembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('diciembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': '"NUVPD"."VM_PORF_CXP"',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VM_PORF_NOMINA',
            fields=[
                ('base', models.CharField(max_length=30)),
                ('doc_compania', models.CharField(max_length=5)),
                ('doc_compania_desc', models.CharField(max_length=30)),
                ('anio', models.CharField(max_length=4)),
                ('periodo', models.CharField(max_length=2)),
                ('doc_tipo', models.CharField(max_length=2)),
                ('doc_tipo_desc', models.CharField(max_length=30)),
                ('doc_numero', models.IntegerField(primary_key=True, serialize=False)),
                ('doc_fecha_lm', models.DateField()),
                ('un_proyecto', models.CharField(max_length=3)),
                ('un_proyecto_desc', models.CharField(max_length=30)),
                ('un_proyecto_zona', models.CharField(max_length=30)),
                ('un_proyecto_tipo', models.CharField(max_length=2)),
                ('un_proyecto_tipo_desc', models.CharField(max_length=60)),
                ('un', models.CharField(max_length=12)),
                ('un_desc', models.CharField(max_length=60)),
                ('cuenta_numero', models.CharField(max_length=29)),
                ('cuenta_desc', models.CharField(max_length=30)),
                ('cuenta_tipo', models.CharField(max_length=3)),
                ('cuenta_tipo_desc', models.CharField(max_length=30)),
                ('cuenta_clase', models.CharField(max_length=3)),
                ('cuenta_clase_desc', models.CharField(max_length=30)),
                ('cuenta_flujo', models.CharField(max_length=3)),
                ('cuenta_flujo_desc', models.CharField(max_length=30)),
                ('cuenta_porf_clase', models.CharField(max_length=3)),
                ('cuenta_porf_clase_desc', models.CharField(max_length=30)),
                ('monto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('enero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('febrero_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('marzo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('abril_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('mayo_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('junio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('julio_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('agosto_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('septiembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('octubre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('noviembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
                ('diciembre_mx', models.DecimalField(decimal_places=4, max_digits=20)),
            ],
            options={
                'db_table': '"NUVPD"."VM_PORF_NOMINA"',
                'managed': False,
            },
        ),
    ]
