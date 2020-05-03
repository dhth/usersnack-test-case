import json

import pytest


@pytest.mark.django_db
def test_get_pizzas(client, add_food_item):
    food_item_1 = add_food_item(
        name="Test Pizza 1",
        item_type="pizza",
        price=16.99,
        img_file="img_file1.png",
    )
    food_item_2 = add_food_item(
        name="Test Pizza 2",
        item_type="pizza",
        price=12.99,
        img_file="img_file2.png",
    )

    resp = client.get(f"/api/pizzas/")

    expected_response = [
        {
            "name": "Test Pizza 1",
            "price": "16.99",
            "images": [{"img_file": "img_file1.png"}],
        },
        {
            "name": "Test Pizza 2",
            "price": "12.99",
            "images": [{"img_file": "img_file2.png"}],
        },
    ]
    assert resp.status_code == 200
    assert resp.data == expected_response
