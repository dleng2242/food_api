# import azure.functions as func
from flask import Flask, request, jsonify
import numpy as np


app = Flask(__name__)


foods = [
    {"id":1, "name": "tomato basil soup", "tags": ["soup"]},
    {"id":2, "name": "chicken noodle soup", "tags": ["soup"]},
    {"id":3, "name": "cauliflower parmesan soup", "tags": ["soup"]},
    {"id":4, "name": "meatball soup", "tags": ["soup"]},
    {"id":5, "name": "beef coriander", "tags": ["soup"]},
    {"id":6, "name": "parsnip soup", "tags": ["soup"]},
    {"id":7, "name": "pesto pasta", "tags": ["pasta"]},
    {"id":8, "name": "broccoli carbonara", "tags": ["pasta"]},
    {"id":9, "name": "bolognese", "tags": ["pasta"]},
    {"id":10, "name": "tomato pasta", "tags": ["pasta"]},
    {"id":11, "name": "sausage fennel pasta", "tags": ["pasta"]},
    {"id":12, "name": "chickpea chorizo stew", "tags": ["stew"]},
    {"id":13, "name": "pork beans kale stew", "tags": ["stew"]},
    {"id":14, "name": "lentil stew", "tags": ["stew"]},
    {"id":15, "name": "beef bouginon", "tags": ["stew"]},
]


@app.route('/', methods=['GET'])
def home():
    welcome_text = """
    <h1>My Food API</h1>
    <p>Welcome to my Food API. A flask API to return food suggestions.</p>
    <br>
    <p>Visit "/api/food/all" to view all the food options, or query the </p>
    <p>data using "/api/food?query=your_query_term&n=number_of_responses".</p>
    """
    return welcome_text

@app.route('/api/food/all', methods=['GET'])
def api_all():
    return jsonify(foods)


@app.route('/api/food', methods=['GET'])
def api_query():
    if 'query' in request.args:
        query = request.args['query']
    else:
        return "Error: No query field provided. Please specify an query.", 404
    
    if 'n' in request.args:
        n = int(request.args['n'])
    else:
        n = 1

    results = []
    for food in foods:
        if query in food["tags"]:
            results.append(food)
    
    if n > len(results):
        return "Error: not enough food items to return request", 404
    
    results = list(np.random.choice(results, size=n, replace=False))

    return jsonify(results)



if __name__ == "__main__":
    app.run(debug=True)
