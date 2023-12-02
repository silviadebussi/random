# Generated by Django 4.2.4 on 2023-12-02 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplic', '0002_remove_cliente_email_endereco_endereco_padrao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacaocategoria',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='estado',
            field=models.CharField(choices=[('GO', 'Goiás'), ('MT', 'Mato Grosso'), ('RN', 'Rio Grande do Norte'), ('PI', 'Piauí'), ('SC', 'Santa Catarina'), ('TO', 'Tocantins'), ('PE', 'Pernambuco'), ('RR', 'Roraima'), ('SP', 'São Paulo'), ('MG', 'Minas Gerais'), ('PR', 'Paraná'), ('DF', 'Distrito Federal'), ('AL', 'Alagoas'), ('RO', 'Rondônia'), ('AP', 'Amapá'), ('ES', 'Espirito Santo'), ('BA', 'Bahia'), ('AC', 'Acre'), ('MS', 'Mato Grosso do Sul'), ('RJ', 'Rio de Janeiro'), ('AM', 'Amazonas'), ('MA', 'Maranhão'), ('RS', 'Rio Grande do Sul'), ('SE', 'Sergipe'), ('PB', 'Paraíba'), ('CE', 'Ceará')], default='MG', max_length=200),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('PE', 'Pedido enviado'), ('PEN', 'Pedido entregue'), ('AG', 'Aguardando Pagamento'), ('PC', 'Pagamento Confirmado')], max_length=100),
        ),
        migrations.AlterField(
            model_name='status',
            name='nome',
            field=models.CharField(choices=[('PE', 'Pedido enviado'), ('PEN', 'Pedido entregue'), ('AG', 'Aguardando Pagamento'), ('PC', 'Pagamento Confirmado')], default='AG', max_length=3),
        ),
    ]