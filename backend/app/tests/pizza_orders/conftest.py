import pytest

from pizza_orders.models import FoodItem


@pytest.fixture(scope="function")
def add_food_item():
    def _add_food_item(name: str, item_type: str, price: float):
        food_item = FoodItem.objects.create(
            name=name, item_type=item_type, price=price
        )
        return food_item

    return _add_food_item
