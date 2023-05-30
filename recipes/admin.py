from django.contrib import admin
from recipes.models import Recipe, RecipeStep, Ingredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "id",
    )

@admin.register(RecipeStep)
class RecipeStepAdmin(admin.ModelAdmin):
    list_display = (
        "step_number",
        "instruction",
        "id",
    )

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        "amount",
        "food_item",
        "id",
    )