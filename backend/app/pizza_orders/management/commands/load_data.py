from django.core.management.base import BaseCommand, CommandError
from pizza_orders.models import FoodItem, FoodImage
import os
import json
import pprint


class Command(BaseCommand):
    help = "Loads data from a JSON file into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "file_name", type=str, help="Path to JSON file containing data"
        )

    def handle(self, *args, **options):
        file_name = options["file_name"]
        self.stdout.write(
            self.style.SUCCESS(f"Loading data from {file_name}...")
        )

        with open(file_name) as jsonfile:
            food_data = json.load(jsonfile)
        pprint.pprint(food_data)

        pizzas = food_data["pizzas"]
        extras = food_data["extras"]

        pizza_objs = []

        for pizza in pizzas:
            pizza_obj = FoodItem(
                name=pizza["name"].strip(),
                item_type="pizza",
                price=pizza["price"],
            )
            pizza_obj.save()
            food_item_img = FoodImage(food_id=pizza_obj, img_file=pizza["img"])
            food_item_img.save()

        self.stdout.write(
            self.style.SUCCESS(f"Saved {len(pizzas)} pizzas to DB.")
        )

        for extra in extras:
            extra_obj = FoodItem(
                name=extra["name"].strip(),
                item_type="extra",
                price=extra["price"],
            )
            extra_obj.save()

        self.stdout.write(
            self.style.SUCCESS(f"Saved {len(extras)} extras to DB.")
        )
