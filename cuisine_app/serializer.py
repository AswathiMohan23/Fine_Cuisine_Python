from rest_framework import serializers

from cuisine_app.models import MenuModel, ItemsModel


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuModel
        fields = ["category", "user_id"]
        # read_only_fields = ["id"]

    def create(self, validated_data):  # overriding default create method of model serializer
        print(validated_data)
        menu = MenuModel.objects.filter(category=validated_data.get('category'),
                                        user_id=self.initial_data.get('user_id'))
        if menu.exists():
            raise Exception("category already exists")
        else:
            menu = MenuModel.objects.create(category=validated_data.get('category'),
                                            user_id=self.initial_data.get('user_id'))

        return menu


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsModel
        fields = ["dish_name", "price","menu"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        print(validated_data)
        dish = validated_data.get('dish_name')
        if not ItemsModel.objects.filter(dish_name=dish).exists():
            items = ItemsModel.objects.create(dish_name=dish,price=self.initial_data.get('price'),
                                              menu_id=self.initial_data.get('menu'))
        return items

