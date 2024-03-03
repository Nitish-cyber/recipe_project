# # recipe_app/urls.py
# from django.urls import path
# from .views import recipe_list, recipe_detail, category_list, category_detail

# app_name = 'recipe_app'

# # urlpatterns = [
# #     path('recipes/', recipe_list, name='recipe_list'),
# #     path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
# #     path('categories/', category_list, name='category_list'),
# #     path('category/<slug:category>/', category_detail, name='category_detail'),
# # ]

# # recipe_app/urls.py
from django.urls import re_path
from .views import recipe_list, recipe_detail, category_list, category_detail

app_name = 'recipe_app'

urlpatterns = [
    re_path(r'^recipes/$', recipe_list, name='recipe_list'),
    re_path(r'^recipe/(?P<recipe_id>\d+)/$', recipe_detail, name='recipe_detail'),
    re_path(r'^categories/$', category_list, name='category_list'),
    re_path(r'^category/(?P<category>[\w-]+)/$', category_detail, name='category_detail'),
]
