from django.shortcuts import render, redirect
from .forms import AddIngredientForm, AddMealForm
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json as simplejson
from .models import Ingredient, Meal

def index(request):
    add_ingredient_form = AddIngredientForm()
    add_meal_form = AddMealForm()
    return render(request, "modern_index.html",{'ingredient_form' : add_ingredient_form, 'meal_form': add_meal_form})

def process_ingredient_form(request):
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        print(form)
    if form.is_valid():
        # process form data
        form.save()
        return redirect('/')

def process_meal_form(request):
    if request.method == 'POST':
        form = AddMealForm(request.POST)
        print(form)
    if form.is_valid():
        # process form data
        form.save()
        return redirect('/')

    return HttpResponse("Didn't work")

def autocomplete_ingredient(request):
    search_qs = Ingredient.objects.filter(name__startswith=request.GET['search'])
    results = []
    for r in search_qs:
        results.append(r.name)
    resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')


def find_meals(request):
    ingredients = request.GET['ingredients']
    ingredient_list = ingredients.split(',')
    meals = list(Meal.objects.filter(ingredients__name__in=ingredient_list))
    meals_json = serializers.serialize('json', meals)
    return HttpResponse(meals_json, content_type='application/json')
