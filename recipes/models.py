from django.db import models
from django.conf import settings

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    picture = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    rating = models.PositiveSmallIntegerField(null=True)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="recipes",
        on_delete=models.CASCADE,
        null=True,
    )

    def __str__(self):
        return self.title

class RecipeStep(models.Model):
    step_number = models.PositiveSmallIntegerField()
    instruction = models.TextField()
    recipe = models.ForeignKey(
        Recipe,
        related_name="steps",
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ["step_number"]

class Ingredient(models.Model):
    amount = models.CharField(max_length=100)
    food_item = models.CharField(max_length=100)
    recipe = models.ForeignKey(
        Recipe,
        related_name="ingredients",
        on_delete=models.CASCADE,
    )
    class Meta:
        ordering = ["food_item"]