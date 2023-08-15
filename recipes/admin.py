from django.contrib import admin
from .models import Category, Recipe
# Register your models here.

# criar uma classe para a área administrativa do model

# @admin.register

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin)
