import pytest

from pizza_orders.models import FoodItem


@pytest.mark.django_db
def test_food_item_model(add_food_item):
    food_item = add_food_item(name="Test Pizza", item_type="pizza", price=16.99)
    assert food_item.name == "Test Pizza"
    assert food_item.item_type == "pizza"
    assert food_item.price == 16.99
    assert food_item.active_in_menu is True
