# Generated by Django 4.2.4 on 2023-08-25 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
        ('garagem', '0002_remove_marca_nacionalidade_remove_veiculo_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='imagem',
            field=models.ManyToManyField(related_name='Imagem', to='uploader.image'),
        ),
    ]