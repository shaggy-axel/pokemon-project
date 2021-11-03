# Generated by Django 3.2.8 on 2021-11-03 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokedexPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Pokemon Name')),
                ('species_id', models.PositiveIntegerField(verbose_name='Pokemon ID')),
                ('height', models.PositiveIntegerField(verbose_name='Pokemon Height')),
                ('weight', models.PositiveIntegerField(verbose_name='Pokemon Weight')),
                ('base_experience', models.PositiveIntegerField(verbose_name='Pokemon Base Exp')),
                ('order', models.PositiveIntegerField(verbose_name='Pokemon Order')),
            ],
            options={
                'verbose_name': 'Pokemon',
                'verbose_name_plural': 'Pokemons',
                'db_table': 'pokedex_pokemons',
                'ordering': ('species_id',),
            },
        ),
    ]
