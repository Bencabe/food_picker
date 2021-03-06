# Generated by Django 3.1.1 on 2021-02-15 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('calories_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('carbs_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('fat_per_unit', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('is_staple', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('instructions', models.JSONField()),
                ('star_rating', models.IntegerField()),
                ('minutes', models.IntegerField()),
                ('ingredients', models.ManyToManyField(related_name='meal_ingredient', to='food_picker.Ingredient')),
            ],
        ),
    ]
