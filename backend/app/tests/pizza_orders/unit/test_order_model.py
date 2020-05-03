import pytest

from pizza_orders.models import Order, OrderDetail


@pytest.mark.django_db
def test_movie_model(add_food_item):
    food_item_1 = add_food_item(
        name="Test Pizza", item_type="pizza", price=16.99
    )
    food_item_1.save()
    food_item_2 = add_food_item(name="Test Extra", item_type="extra", price=1.0)
    food_item_2.save()

    user_name = "Dhruv"
    user_address = "Wien"
    order = Order(user_name=user_name, user_address=user_address)
    order.save()

    order_detail_1 = OrderDetail(
        order_id=order, food_item=food_item_1, quantity=1
    )
    order_detail_1.save()
    order_detail_2 = OrderDetail(
        order_id=order, food_item=food_item_2, quantity=2
    )
    order_detail_2.save()

    assert order.user_name == user_name
    assert order.user_address == user_address
    assert order.status == "initiated"

    assert order_detail_1.order_id == order
    assert order_detail_1.food_item == food_item_1
    assert order_detail_1.quantity == 1

    assert order_detail_2.order_id == order
    assert order_detail_2.food_item == food_item_2
    assert order_detail_2.quantity == 2
