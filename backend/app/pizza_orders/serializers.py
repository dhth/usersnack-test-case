from rest_framework import serializers
from .models import Movie, FoodItem, FoodImage, Order, OrderDetail


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


class FoodItemSerializer(serializers.ModelSerializer):
    images = FoodImageSerializer(many=True, read_only=True)

    class Meta:
        model = FoodItem
        fields = ["name", "price", "images"]
        # read_only_fields = ["name", "price", "images"]
        # list_serializer_class = StoreRotationListSerializer

    # def to_representation(self, instance):
    #     """Convert `username` to lowercase."""
    #     ret = super().to_representation(instance)
    #     # ret['hola'] = "watup"
    #     return {"data": ret}
