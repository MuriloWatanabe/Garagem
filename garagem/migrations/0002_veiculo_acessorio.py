# Generated by Django 4.2 on 2023-08-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='acessorio',
            field=models.ManyToManyField(related_name='Acessórios', to='garagem.acessorio'),
        ),
    ]
