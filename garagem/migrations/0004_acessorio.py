# Generated by Django 4.1.7 on 2023-03-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0003_marca_delete_marcas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acessorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]
