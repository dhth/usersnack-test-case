import pytest


@pytest.mark.django_db
def test_get_extras(client, add_food_item):
    food_item_1 = add_food_item(
        name="Test Pizza 1",
        item_type="pizza",
        price=16.99,
        img_file="img_file1.png",
    )
    for i in range(1, 4):
        extra = add_food_item(
            name=f"Test Extra {i}", item_type="extra", price=2.0
        )

    resp = client.get(f"/api/extras/")

    response = resp.json()
    print(response)
    for extra in response["extras"]:
        del extra["id"]

    expected_response = [
        {"name": "Test Extra 1", "price": "2.00"},
        {"name": "Test Extra 2", "price": "2.00"},
        {"name": "Test Extra 3", "price": "2.00"},
    ]

    assert resp.status_code == 200
    assert response["extras"] == expected_response
