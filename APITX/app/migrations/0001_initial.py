# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TxcActividad',
            fields=[
                ('idactividad', models.AutoField(db_column='idActividad', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('descripcion', models.TextField()),
                ('fecha', models.DateTimeField()),
                ('lugar', models.CharField(max_length=100)),
                ('ubicacion', models.CharField(blank=True, max_length=250, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txc_actividad',
            },
        ),
        migrations.CreateModel(
            name='TxcArticulo',
            fields=[
                ('idarticulo', models.AutoField(db_column='idArticulo', primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('numero', models.IntegerField(blank=True, null=True)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'txc_articulo',
            },
        ),
        migrations.CreateModel(
            name='TxcCapitulo',
            fields=[
                ('idcapitulo', models.AutoField(db_column='idCapitulo', primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txc_capitulo',
            },
        ),
        migrations.CreateModel(
            name='TxcoConsejo',
            fields=[
                ('idconsejo', models.AutoField(db_column='idConsejo', primary_key=True, serialize=False)),
                ('consejo', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txco_consejo',
            },
        ),
        migrations.CreateModel(
            name='TxcoFecha',
            fields=[
                ('idfecha', models.AutoField(db_column='idFecha', primary_key=True, serialize=False)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('consejo', models.ForeignKey(db_column='Consejo_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxcoConsejo')),
            ],
            options={
                'db_table': 'txco_fecha',
            },
        ),
        migrations.CreateModel(
            name='TxcPregunta',
            fields=[
                ('idpregunta', models.AutoField(db_column='idPregunta', primary_key=True, serialize=False)),
                ('pregunta', models.TextField(blank=True, null=True)),
                ('respuesta', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txc_pregunta',
            },
        ),
        migrations.CreateModel(
            name='TxcPreguntaarticulo',
            fields=[
                ('idpreguntaarticulo', models.AutoField(db_column='idPreguntaArticulo', primary_key=True, serialize=False)),
                ('articulo', models.ForeignKey(db_column='Articulo_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxcArticulo')),
                ('pregunta', models.ForeignKey(db_column='Pregunta_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxcPregunta')),
            ],
            options={
                'db_table': 'txc_preguntaarticulo',
            },
        ),
        migrations.CreateModel(
            name='TxcTitulo',
            fields=[
                ('idtitulo', models.AutoField(db_column='idTitulo', primary_key=True, serialize=False)),
                ('titulo', models.CharField(blank=True, max_length=100, null=True)),
                ('numero', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txc_titulo',
            },
        ),
        migrations.CreateModel(
            name='TxdBus',
            fields=[
                ('idbus', models.AutoField(db_column='idBus', primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=8)),
                ('color', models.CharField(max_length=20)),
                ('modelo', models.CharField(blank=True, max_length=45, null=True)),
                ('marca', models.CharField(max_length=20)),
                ('numbus', models.IntegerField()),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_bus',
            },
        ),
        migrations.CreateModel(
            name='TxdChofer',
            fields=[
                ('idchofer', models.AutoField(db_column='idChofer', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('dpi', models.IntegerField()),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
                ('licencia', models.CharField(max_length=11)),
                ('tipolicencia', models.CharField(blank=True, db_column='tipoLicencia', max_length=2, null=True)),
                ('nolicencia', models.IntegerField(blank=True, db_column='noLicencia', null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_chofer',
            },
        ),
        migrations.CreateModel(
            name='TxdDenuncia',
            fields=[
                ('iddenuncia', models.BigAutoField(db_column='idDenuncia', primary_key=True, serialize=False)),
                ('idhash', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('fechahora', models.DateTimeField(blank=True, null=True)),
                ('placa', models.CharField(blank=True, max_length=7, null=True)),
                ('chofer', models.ForeignKey(blank=True, db_column='Chofer_id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdChofer')),
            ],
            options={
                'db_table': 'txd_denuncia',
            },
        ),
        migrations.CreateModel(
            name='TxdDia',
            fields=[
                ('iddia', models.AutoField(db_column='idDia', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'txd_dia',
            },
        ),
        migrations.CreateModel(
            name='TxdDiahorario',
            fields=[
                ('iddiahorario', models.AutoField(db_column='idDiaHorario', primary_key=True, serialize=False)),
                ('dia', models.ForeignKey(db_column='Dia_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdDia')),
            ],
            options={
                'db_table': 'txd_diahorario',
            },
        ),
        migrations.CreateModel(
            name='TxdDiahorariodetalle',
            fields=[
                ('iddiahorariodetalle', models.AutoField(db_column='idDiaHorarioDetalle', primary_key=True, serialize=False)),
                ('bus', models.ForeignKey(db_column='Bus_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdBus')),
                ('chofer', models.ForeignKey(db_column='Chofer_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdChofer')),
                ('diahorario', models.ForeignKey(db_column='DiaHorario_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdDiahorario')),
            ],
            options={
                'db_table': 'txd_diahorariodetalle',
            },
        ),
        migrations.CreateModel(
            name='TxdDuenio',
            fields=[
                ('idduenio', models.AutoField(db_column='idDuenio', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellidos', models.CharField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('dpi', models.IntegerField()),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('foto', models.CharField(max_length=100)),
                ('estado', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_duenio',
            },
        ),
        migrations.CreateModel(
            name='TxdHorario',
            fields=[
                ('idhorario', models.AutoField(db_column='idHorario', primary_key=True, serialize=False)),
                ('horainicio', models.TimeField()),
                ('horafin', models.TimeField()),
                ('duenio', models.ForeignKey(db_column='Duenio_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdDuenio')),
            ],
            options={
                'db_table': 'txd_horario',
            },
        ),
        migrations.CreateModel(
            name='TxdRecurso',
            fields=[
                ('idrecurso', models.AutoField(db_column='idRecurso', primary_key=True, serialize=False)),
                ('direccion', models.CharField(blank=True, max_length=100, null=True)),
                ('denuncia', models.ForeignKey(db_column='Denuncia_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdDenuncia')),
            ],
            options={
                'db_table': 'txd_recurso',
            },
        ),
        migrations.CreateModel(
            name='TxdRuta',
            fields=[
                ('idruta', models.AutoField(db_column='idRuta', primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('recorrido', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'txd_ruta',
            },
        ),
        migrations.CreateModel(
            name='TxdTipodenuncia',
            fields=[
                ('idtipodenuncia', models.AutoField(db_column='idTipodenuncia', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'txd_tipodenuncia',
            },
        ),
        migrations.CreateModel(
            name='TxuRol',
            fields=[
                ('idrol', models.AutoField(db_column='idRol', primary_key=True, serialize=False)),
                ('rol', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'txu_rol',
            },
        ),
        migrations.CreateModel(
            name='TxuUsuario',
            fields=[
                ('idpersona', models.AutoField(db_column='idPersona', primary_key=True, serialize=False)),
                ('nombre', models.IntegerField(blank=True, null=True)),
                ('direccion', models.CharField(blank=True, max_length=45, null=True)),
                ('telefono', models.CharField(blank=True, max_length=8, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('dpi', models.CharField(blank=True, max_length=13, null=True)),
                ('estado', models.IntegerField(blank=True, null=True)),
                ('usuario', models.CharField(blank=True, max_length=45, null=True)),
                ('contrasenia', models.CharField(blank=True, max_length=45, null=True)),
                ('rol', models.ForeignKey(db_column='Rol_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxuRol')),
            ],
            options={
                'db_table': 'txu_usuario',
            },
        ),
        migrations.AddField(
            model_name='txddiahorario',
            name='horario',
            field=models.ForeignKey(db_column='Horario_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdHorario'),
        ),
        migrations.AddField(
            model_name='txddenuncia',
            name='tipodenuncia',
            field=models.ForeignKey(db_column='Tipodenuncia_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdTipodenuncia'),
        ),
        migrations.AddField(
            model_name='txdchofer',
            name='duenio',
            field=models.ForeignKey(db_column='Duenio_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdDuenio'),
        ),
        migrations.AddField(
            model_name='txdbus',
            name='duenio',
            field=models.ForeignKey(db_column='Duenio_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdDuenio'),
        ),
        migrations.AddField(
            model_name='txdbus',
            name='ruta',
            field=models.ForeignKey(db_column='Ruta_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxdRuta'),
        ),
        migrations.AddField(
            model_name='txccapitulo',
            name='titulo_0',
            field=models.ForeignKey(db_column='Titulo_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxcTitulo'),
        ),
        migrations.AddField(
            model_name='txcarticulo',
            name='capitulo',
            field=models.ForeignKey(db_column='Capitulo_id', on_delete=django.db.models.deletion.DO_NOTHING, to='app.TxcCapitulo'),
        ),
    ]
