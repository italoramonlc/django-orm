# Generated by Django 4.2.1 on 2023-05-19 14:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_endereco_cliente_endereco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endereco',
            old_name='ciadade',
            new_name='cidade',
        ),
    ]