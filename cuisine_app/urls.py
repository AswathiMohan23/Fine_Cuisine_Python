from django.urls import path

from cuisine_app import views

urlpatterns = [
    path('menu', views.Cuisine_Menu.as_view(), name="menu"),
    path('menu/<int:id>', views.Cuisine_Menu.as_view(), name='menu'),
    path('', views.CuisineItems.as_view(), name="items"),

]
