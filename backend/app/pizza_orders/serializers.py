from rest_framework import serializers
from .models import Movie, FoodItem, FoodImage, Order, OrderDetail
from django.db import transaction


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )


# class StoreRotationListSerializer(serializers.ListSerializer):

#     def to_representation(self, data):
#         repr = super(StoreRotationListSerializer, self).to_representation(data)
#         return {'data': repr}


class FoodImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodImage
        fields = ["img_file"]


class PizzaSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(many=True, read_only=True)

    class Meta:
        model = FoodItem
        fields = ["id", "name", "price", "images"]
        # read_only_fields = ["name", "price", "images"]
        # list_serializer_class = StoreRotationListSerializer

    # def to_representation(self, instance):
    #     """Convert `username` to lowercase."""
    #     ret = super().to_representation(instance)
    #     # ret['hola'] = "watup"
    #     return {"data": ret}


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ["id", "name", "price"]


class OrderExtraSerializer(serializers.Serializer):
    extra = serializers.PrimaryKeyRelatedField(
        queryset=FoodItem.objects.filter(item_type="extra"), many=False
    )
    quantity = serializers.IntegerField(required=True)


class OrderSerializer(serializers.Serializer):

    base_pizza = serializers.PrimaryKeyRelatedField(
        queryset=FoodItem.objects.filter(item_type="pizza"), many=False
    )
    extras = OrderExtraSerializer(many=True, required=False)
    user_name = serializers.CharField(max_length=200, required=True)
    user_address = serializers.CharField(max_length=200, required=True)

    def create(self, validated_data):
        with transaction.atomic():
            new_order = Order(
                user_name=validated_data["user_name"],
                user_address=validated_data["user_address"],
            )

            new_order.save()

            new_order_detail = OrderDetail(
                order_id=new_order,
                food_item=validated_data["base_pizza"],
                quantity=1,
            )
            new_order_detail.save()
            for extra in validated_data["extras"]:
                extra_row = OrderDetail(
                    order_id=new_order,
                    food_item=extra["extra"],
                    quantity=extra["quantity"],
                )
                extra_row.save()
        return new_order
