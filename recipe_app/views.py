# recipe_app/views.py
from django.http import HttpResponse

def recipe_list(request):
    return HttpResponse('List of Recipes')

def recipe_detail(request, recipe_id):
    return HttpResponse(f'Details of Recipe #{recipe_id}')

def category_list(request):
    return HttpResponse('List of Categories')

def category_detail(request, category):
    return HttpResponse(f'Details of Category: {category}')
