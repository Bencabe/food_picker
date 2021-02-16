from django.shortcuts import render, redirect
from .forms import AddIngredientForm
from django.http import HttpResponse,JsonResponse

def index(request):
    add_ingredient_form = AddIngredientForm()
    return render(request, "modern_index.html",{'ingredient_form' : add_ingredient_form})

def process_ingredients_form(request):
    if request.method == 'POST':
        form = AddIngredientForm(request.POST)
        print(form)
    if form.is_valid():
        # process form data
        print('inside')
        form.save()
        return redirect('/')

    else:
        add_ingredient_form = AddIngredientForm()

    return HttpResponse("Didn't work")
