from django.db import models

from Fine_Cuisine import settings


class MenuModel(models.Model):
    category = models.CharField(max_length=150)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = "menu_table"


class ItemsModel(models.Model):
    dish_name = models.CharField(max_length=150)
    price = models.CharField(max_length=150)
    menu = models.ForeignKey(MenuModel, on_delete=models.CASCADE, related_name='items')

    class Meta:
        db_table = "items_table"
