from . import views
from django.urls import path

app_name = "mysite"
urlpatterns = [
    path("", views.index, name="home"),
    path("category/<int:categoryId>", views.category, name="category"),
    path("budget/<int:budgetId>", views.budget, name="budget"),
]
