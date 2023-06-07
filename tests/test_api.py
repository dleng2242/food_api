import ast
import pytest

import FoodApi


@pytest.fixture
def client():
    FoodApi.app.config['TESTING'] = True
    with FoodApi.app.test_client() as client:
        yield client

STEW_OPTIONS = [
    'chickpea chorizo stew', 
    'pork beans kale stew', 
    'lentil stew', 
    'beef bouginon',
]

def test_get_all_stews(client):
    response = client.get("/food/stew/0")
    test = response.get_json()
    target = {"data": "['chickpea chorizo stew', 'pork beans kale stew', 'lentil stew', 'beef bouginon']"}
    assert test == target

def test_get_a_stew(client):
    response = client.get("/food/stew")
    test = response.get_json()
    # literal string evaluation on list
    test_food_items = ast.literal_eval(test["data"])
    assert len(test_food_items) == 1
    assert test_food_items[0] in STEW_OPTIONS

def test_get_two_stews(client):
    response = client.get("/food/stew/2")
    test = response.get_json()
    # literal string evaluation on list
    test_food_items = ast.literal_eval(test["data"])
    assert len(test_food_items) == 2
    assert test_food_items[0] in STEW_OPTIONS
    assert test_food_items[1] in STEW_OPTIONS
