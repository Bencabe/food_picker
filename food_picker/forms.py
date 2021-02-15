from .models import Ingredient,Meal
from django import forms

class AddIngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name", "calories_per_unit","protein_per_unit","carbs_per_unit","fat_per_unit","is_staple"]