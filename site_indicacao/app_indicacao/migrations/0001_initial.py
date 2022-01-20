# Generated by Django 4.0.1 on 2022-01-18 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('fone_celular', models.CharField(max_length=20)),
                ('fone_whatsapp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=200)),
                ('uf', models.CharField(max_length=2)),
                ('obs', models.TextField(blank=True, max_length=400)),
                ('cupom', models.CharField(max_length=20)),
                ('data_cadastro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('fone_celular', models.CharField(max_length=20)),
                ('fone_whatsapp', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('cidade', models.CharField(choices=[('1', 'Felipe Guerra'), ('2', 'Gov. Dix-Sept Rosado')], max_length=200)),
                ('uf', models.CharField(choices=[('RN', 'RN')], max_length=2)),
                ('obs', models.TextField(blank=True, max_length=400)),
                ('data_cadastro', models.DateField(auto_now_add=True)),
                ('cliente_ativado', models.BooleanField(default=False)),
                ('cupom', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='app_indicacao.cupom')),
            ],
        ),
    ]
