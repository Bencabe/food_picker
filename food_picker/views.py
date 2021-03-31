from django.shortcuts import render, redirect
from .forms import AddIngredientForm, AddMealForm
from django.http import HttpResponse,JsonResponse
from django.core import serializers
import json as simplejson
from .models import Ingredient, Meal
from django.db.models import Count

def index(request):
    # used to serve up index.html
    add_ingredient_form = AddIngredientForm()
    add_meal_form = AddMealForm()
    return render(request, "index.html",{'ingredient_form' : add_ingredient_form, 'meal_form': add_meal_form})

def process_ingredient_form(request):
    # used to process the form for adding new ingredients
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        print(form)
    if form.is_valid():
        # process form data
        form.save()
        return redirect('/')

def process_meal_form(request):
    # used to process the form for adding new meals
    print('=================== Post ====================')
    print(request.POST)
    print('=============================================')
    if request.method == 'POST':
        form = AddMealForm(request.POST)
        print('===================Meal Form:====================')
        print(form)
        print('=================================================')
    if form.is_valid():
        # process form data
        form.save()
        return redirect('/')

    return HttpResponse("Didn't work")

def autocomplete_ingredient(request):
    # used to provide list of potential ingredients in ingredient picker based on first few letters 
    print(request)
    search_qs = Ingredient.objects.filter(name__startswith=request.GET['search'])
    results = []
    for r in search_qs:
        results.append(r.name)
    resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')


def find_meals(request):
    # used to find appropriate meals based on ingredients chosen by user 
    ingredients = request.GET['ingredients']
    # split ingredients into list and remove trailing white spaces
    ingredient_list = [x.strip() for x in ingredients.split(',')]
    # get meals which contain ingredients listed
    # meal_query = Meal.objects.filter(ingredients__name__in=ingredient_list)
    meal_query = Meal.objects.annotate(count=Count('ingredients')).filter(count=len(ingredient_list))
    for ingredient in ingredient_list:
        meal_query = meal_query.filter(ingredients__name=ingredient)
    meals_json = serializers.serialize('json', meal_query)
    return HttpResponse(meals_json, content_type='application/json')
