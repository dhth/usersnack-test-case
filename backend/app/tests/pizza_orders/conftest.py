import pytest

from pizza_orders.models import FoodItem, FoodImage


@pytest.fixture(scope="function")
def add_food_item():
    def _add_food_item(name: str, item_type: str, price: float, img_file=None):
        food_item = FoodItem.objects.create(
            name=name, item_type=item_type, price=price
        )
        if img_file is not None:
            food_image = FoodImage(food_id=food_item, img_file=img_file)
            food_image.save()
        return food_item

    return _add_food_item


@pytest.fixture(scope="function")
def add_multiple_items():
    def _add_multiple_items():
        food_item_1 = FoodItem.objects.create(
            name="Test Pizza 1", item_type="pizza", price=16.99
        )

        food_item_2 = FoodItem.objects.create(
            name="Test Extra 1", item_type="extra", price=2.0
        )

        food_item_3 = FoodItem.objects.create(
            name="Test Extra 2", item_type="extra", price=1.0
        )
        return (food_item_1, food_item_2, food_item_3)

    return _add_multiple_items
