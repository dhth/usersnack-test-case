import pytest


@pytest.mark.django_db
def test_correct_order_retrieval(client, add_multiple_items):
    """
    Tests if details for a specific order are correct, including
    individual components, and total amount.
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

    resp2 = client.get(f"/api/orders/{new_order_id}/")

    response_2 = resp2.json()

    expected_total = (
        food_item_1.price + food_item_2.price * 2 + food_item_3.price * 3
    )

    assert resp2.status_code == 200
    assert response_2["success"] is True
    assert response_2["total"] == str(expected_total)
