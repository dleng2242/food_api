import azure.functions as func
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import random
import os


app = Flask(__name__)
api = Api(app)

food_put_parser = reqparse.RequestParser()
food_put_parser.add_argument(
    "food_item", type=str, help="Please supply a food item name", required=True
)

food_delete_parser = reqparse.RequestParser()
food_delete_parser.add_argument(
    "food_item", type=str, help="Please supply a food item name", required=True
)

foods = {
    "soup": [
        "tomato basil soup",
        "chicken noodle soup",
        "cauliflower parmesan soup",
        "meatball soup",
        "beef coriander",
        "parsnip soup",
    ],
    "pasta": [
        "pesto pasta",
        "broccoli carbonara",
        "bolognese",
        "tomato pasta",
        "prawn tomato pasta",
        "sausage fennel pasta",
    ],
    "stew": [
        "chickpea chorizo stew",
        "pork beans kale stew",
        "lentil stew",
        "beef bouginon",
    ],
}


def abort_if_food_type_not_in_foods(food_type):
    if food_type not in foods:
        abort(404, message="Could not find food type...")


def abort_if_food_item_already_in_food_type_in_foods(food_type, food_item):
    if food_item in foods.get(food_type, []):
        abort(409, message=f"{food_item} already exists in {food_type} food type...")


def abort_if_food_item_not_in_food_type_in_foods(food_type, food_item):
    if food_item not in foods[food_type]:
        abort(404, message=f"{food_item} not found in {food_type} food type...")


class Food(Resource):
    def get(self, food_type, num=1):
        abort_if_food_type_not_in_foods(food_type)
        if num > 0:
            random_food = random.choices(foods[food_type], k=num)
        elif num == 0:
            random_food = foods[food_type]
        else:
            abort(400, message="Number provided was not a valid input...")
        return {"data": f"{random_food}"}

    def put(self, food_type):
        args = food_put_parser.parse_args()
        abort_if_food_item_already_in_food_type_in_foods(food_type, args["food_item"])
        foods[food_type] = foods.get(food_type, []) + [args["food_item"]]
        return {"args": args}, 201

    def delete(self, food_type):
        args = food_delete_parser.parse_args()
        abort_if_food_item_not_in_food_type_in_foods(food_type, args["food_item"])
        foods[food_type].remove(args["food_item"])
        return "", 204


api.add_resource(
    Food, "/food/<string:food_type>", "/food/<string:food_type>/<int:num>",
)

if __name__ == "__main__":
    app.run(debug=True)
