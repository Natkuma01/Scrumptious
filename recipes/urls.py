from django.urls import path
from recipes.views import show_recipe, recipe_list, create_recipe, edit_recipe, my_recipe_list

urlpatterns = [
    path("<int:id>/", show_recipe, name="show_recipe"),
    path("", recipe_list, name="recipe_list"),
    path("create/", create_recipe, name="create_recipe"),
    path("<int:id>/edit/", edit_recipe, name="edit_recipe"),
    path("mine/", my_recipe_list, name="my_recipe_list"),
]
