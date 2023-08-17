# from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, get_list_or_404, get_object_or_404
from .utils.recipes.factory import make_recipe

from recipes.models import Recipe


def index(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
        # 'recipes': [make_recipe() for _ in range(10)],
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


def category(request, category_id):
    # recipes = Recipe.objects.filter(
    #    category__id=category_id, is_published=True).order_by('-id')
    # if not recipes:
    #    raise Http404('No found')
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name} - Category | '
    })
