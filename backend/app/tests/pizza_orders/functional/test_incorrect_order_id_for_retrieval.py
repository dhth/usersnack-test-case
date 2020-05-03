import pytest


@pytest.mark.django_db
def test_incorrect_order_id_for_retrieval(client, add_multiple_items):
    """
    Tests if 404 is returned for a non-existent order ID.
    """
    (food_item_1, food_item_2, food_item_3) = add_multiple_items()

    resp = client.post(
        "/api/createorder/",
        {
            "base_pizza": food_item_1.id,
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
    new_order_id = response["order"]["id"]

    resp2 = client.get(f"/api/orders/99/")

    response_2 = resp2.json()

    assert resp2.status_code == 404
