from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage, name="HomePage"),
    path('cards',views.category,name="cards"),
    path('review',views.review,name="review"),
    path("<single_slug>", views.single_slug, name="single_slug"),
]
