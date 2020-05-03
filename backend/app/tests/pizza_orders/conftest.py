import pytest

from pizza_orders.models import FoodItem, FoodImage


@pytest.fixture(scope="function")
def add_food_item():
    def _add_food_item(
        name: str, item_type: str, price: float, img_file="test_file.png"
    ):
        food_item = FoodItem.objects.create(
            name=name, item_type=item_type, price=price
        )
        food_image = FoodImage(food_id=food_item, img_file=img_file)
        food_image.save()
        return food_item

    return _add_food_item
