from django.urls import path

from . import views

# recipes:recipe
app_name = 'recipes'

urlpatterns = [
    # path('home/', views.index, name="index"),
    # path('about/', views.about, name="about"),
    # path('contact/', views.contact, name="contact"),
    path('', views.index, name="index"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
