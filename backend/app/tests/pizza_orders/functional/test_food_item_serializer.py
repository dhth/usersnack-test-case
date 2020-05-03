# from pizza_orders.serializers import PizzaSerializer


# def test_valid_food_item_serializer():
#     valid_serializer_data = {
#         "name": "Test Pizza",
#         "item_type": "pizza",
#         "price": 16.99,
#     }
#     serializer = FoodItemSerializer(data=valid_serializer_data)
#     assert serializer.is_valid()
#     assert serializer.validated_data == valid_serializer_data
#     assert serializer.data == valid_serializer_data
#     assert serializer.errors == {}


# def test_invalid_movie_serializer():
#     invalid_serializer_data = {
#         "title": "Raising Arizona",
#         "genre": "comedy"
#     }
#     serializer = MovieSerializer(data=invalid_serializer_data)
#     assert not serializer.is_valid()
#     assert serializer.validated_data == {}
#     assert serializer.data == invalid_serializer_data
#     assert serializer.errors == {"year": ["This field is required."]}
