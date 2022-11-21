from django.shortcuts import render
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'chai': {
        'вода, мл': 350,
        'чайный пакетик, шт': 1
    },
}


def home_view(request):
    return HttpResponse('Доступные рецепты: омлет (omlet), паста (pasta), бутерброд (buter), чай (chai).')


def recipe(request, recipe):
    quantity = int(request.GET.get("servings", 1))
    recipe = DATA[recipe]
    for ingredient, amount in recipe.items():
        recipe[ingredient] = amount * quantity
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)