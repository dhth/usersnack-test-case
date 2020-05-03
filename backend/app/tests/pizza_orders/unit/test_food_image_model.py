import pytest

from pizza_orders.models import FoodImage


@pytest.mark.django_db
def test_movie_model(add_food_item):
    food_item = add_food_item(name="Test Pizza", item_type="pizza", price=16.99)
    food_image = FoodImage(food_id=food_item, img_file="test_pizza_image.png")
    assert food_image.food_id == food_item
    assert food_image.img_file == "test_pizza_image.png"
