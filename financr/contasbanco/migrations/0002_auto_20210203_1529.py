# Generated by Django 3.1.5 on 2021-02-03 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contasbanco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas_bancarias',
            name='nome_banco',
            field=models.CharField(max_length=20),
        ),
    ]
