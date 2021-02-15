from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50,unique=True)
    calories_per_unit = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    protein_per_unit = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    carbs_per_unit = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    fat_per_unit = models.DecimalField(default=0,max_digits=5,decimal_places=2)
    is_staple = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=50,unique=True)
    instructions = models.JSONField()
    ingredients = models.ManyToManyField(Ingredient,related_name='meal_ingredient')
    star_rating = models.IntegerField()
    minutes = models.IntegerField()
    def __str__(self):
        return self.name