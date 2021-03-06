# Generated by Django 3.1.2 on 2020-11-01 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_auto_20201101_1709'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='grupo',
            field=models.CharField(choices=[('ACES', 'Acessórios'), ('PCIM', 'Partes de cima'), ('PBAI', 'Partes de baixo')], default='ACES', max_length=300, verbose_name='Grupos'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('CAMT', 'Camisetas'), ('BLUS', 'Blusinhas'), ('CAMI', 'Camisas'), ('SUCA', 'Suéteres e cardigans'), ('BLJC', 'Blazers, jaquetas e casacos'), ('COLQ', 'Coletes e quimonos'), ('REGA', 'Regatas'), ('SHBE', 'Shorts e bermudas'), ('CALC', 'Calças'), ('VEST', 'Vestidos'), ('SAIA', 'Saias'), ('MAIC', 'Meias-calças'), ('CACP', 'Cachecóis e pashminas'), ('LENC', 'Lenços'), ('BOLS', 'Bolsas'), ('SAPT', 'Sapatos'), ('MEIA', 'Meias')], default='CAMT', max_length=300, verbose_name='Categorias'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='status',
            field=models.BooleanField(verbose_name='Disponível'),
        ),
    ]
