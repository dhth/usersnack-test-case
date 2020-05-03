# Usersnack

## Tech Stack

- **Django**: Backend
- **Django Rest Framework**: addons for Django
- **Postgres**: Database

## Other tools
- **Pytest**: testing framework
- **Flake8**: Linter
- **Black**: Formatter

## Live app
A live version of the service is running on Heroku here: [https://evening-scrubland-88960.herokuapp.com](https://evening-scrubland-88960.herokuapp.com/api/pizzas/). It might take a few seconds for the service to spin up after a period of inactivity.
## Local setup

- Change permissions on entrypoint.sh
    ```bash
    chmod +x backend/app/entrypoint.sh
    ```
- Run containers
    ```
    docker-compose up -d
    ```

## Endpoints

- `/api/pizzas/`
    
    This endpoint is supposed to provide data for the Pizza list view.

    ![](/imgs/pizza-list.png)

    ```curl
    curl --location --request GET 'http://127.0.0.1:8000/api/pizzas/'
    ```
- `/api/extras/`
    
    This endpoint is supposed to provide data for the extra dropdowns.

    ![](/imgs/extra-dropdown.png)

    ```curl
    curl --location --request GET 'http://127.0.0.1:8000/api/extras/'
    ```

- `/api/createorder/`
    
    This endpoint is for creating a new order.

    ```curl
    curl --location --request POST 'http://127.0.0.1:8000/api/createorder/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "base_pizza": 1,
        "extras": [
            {
                "extra": 15,
                "quantity": 1
            },
            {
                "extra": 16,
                "quantity": 5
            }
        ],
        "user_name": "Dhruv",
        "user_address": "Wien"
    }'
    ```

- `/api/orders/<id>/`
    
    This endpoint returns the details of a specific order, including component items, and total price.

    ```curl
    curl --location --request GET 'http://127.0.0.1:8000/api/orders/1'
    ```

- `/api/orders/`
    
    This endpoint returns all orders.

    ```curl
    curl --location --request GET 'http://127.0.0.1:8000/api/orders/'
    ```

## Tests

```
docker-compose exec backend pytest tests
```

## To Do

- Add Swagger documentation using [drf-yasg](https://github.com/axnsan12/drf-yasg).
- Change `item_type` (in table `FoodItem`) to a relationship instead of CharField. (done to save time).