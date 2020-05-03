import pytest


@pytest.mark.django_db
def test_create_order(client, add_multiple_items):

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

    assert resp.status_code == 200
    assert response["success"] is True
    assert response["order"]["user_name"] == "Dhruv"
    assert response["order"]["user_address"] == "Gotham"
