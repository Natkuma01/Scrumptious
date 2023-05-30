from django import forms
from recipes.models import Recipe

class RecipeForm(forms.ModelForm):
    email_address = forms.EmailField(max_length=300)
    class Meta:
        model = Recipe
        fields = [
            "title",
            "picture",
            "description",
        ]