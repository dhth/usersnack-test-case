import pytest
from usersnack import settings as app_settings


@pytest.mark.django_db
def test_get_pizzas(client, add_food_item):
    """
    Tests correctness of pizzas returned, based on data contained
    in the DB.
    """
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
    response = resp.json()

    for pizza in response["pizzas"]:
        del pizza["id"]

    expected_response = [
        {
            "name": "Test Pizza 1",
            "price": "16.99",
            "images": [
                {"img_file": f"{app_settings.IMG_STATIC_DIR}img_file1.png"}
            ],
        },
        {
            "name": "Test Pizza 2",
            "price": "12.99",
            "images": [
                {"img_file": f"{app_settings.IMG_STATIC_DIR}img_file2.png"}
            ],
        },
    ]
    assert resp.status_code == 200
    assert response["pizzas"] == expected_response
