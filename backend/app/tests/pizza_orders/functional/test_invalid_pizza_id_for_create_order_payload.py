import json

import pytest


@pytest.mark.django_db
def test_invalid_pizza_id_for_create_order_payload(client, add_multiple_items):
    """
    Tests if 400 is returned for a non-existent pizza during
    order creation.
    """
    (food_item_1, food_item_2, food_item_3) = add_multiple_items()

    resp = client.post(
        "/api/createorder/",
        {
            "base_pizza": 99,
            "extras": [
                {"extra": food_item_2.id, "quantity": 2},
                {"extra": food_item_3.id, "quantity": 3},
            ],
            "user_name": "Dhruv",
            "user_address": "Gotham",
        },
        content_type="application/json",
    )
    response = resp.json()

    assert resp.status_code == 400
    assert response["success"] is False
