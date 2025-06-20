# Generated by Django 5.2.1 on 2025-06-12 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basearq', '0003_avatar_delete_administrador_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquitecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='obras/')),
            ],
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('arquitectos', models.ManyToManyField(to='basearq.arquitecto')),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basearq.ciudad')),
            ],
        ),
        migrations.DeleteModel(
            name='NuevasObras',
        ),
        migrations.AddField(
            model_name='imagenobra',
            name='obra',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='imagen', to='basearq.obra'),
        ),
    ]
