#import library for api creation
#jsonify package is to convert our python object(list) to json format

from flask import Flask, jsonify, request
from http import HTTPStatus


#creating an instance of the flask class
app = Flask(__name__)

#defining recipelist. they are stored in local memory as list
recipes = [
    {
        'id': 1,
        'name': 'Sandwitch',
        'description': 'This is a sandwitch recipe'
    },
    {
        'id': 2,
        'name': 'Jam Jelly',
        'description': 'This is a Jelly recipe'
    }
]

#route decorator to tell flask to route the method
@app.route('/')
def hello_world():
    return 'Hello'


@app.route('/recipes', methods=['GET'])
def get_recipes():
    return jsonify({'data': recipes})

@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if recipe:
        return jsonify(recipe)

    return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND


@app.route('/recipes', methods=['post'])
def create_recipe():
   data = request.get_json()

   name = data.get('name')
   description = data.get('description')

   recipe = {
       'id': len(recipes) + 1,
       'name': name,
       'description': description
   }

   recipes.append(recipe)

   return jsonify(recipe), HTTPStatus.CREATED

@app.route('/recipes/<int:recipe_id>', methods=['put'])
def update_recipe(recipe_id):
   recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)


   if not recipe:
       return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    
   data = request.get_json()

   recipe.update(
       {
           'name': data.get('name'),
           'description': data.get('description')        
       }
   )

   return jsonify(recipe)


@app.route('/recipes/<int:recipe_id>', methods=['delete'])
def delete_recipe(recipe_id):
   recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)


   if not recipe:
       return jsonify({'message': 'recipe not found'}), HTTPStatus.NOT_FOUND
    
   data = request.get_json()

   recipe.remove(
       {
           'name': data.get('name'),
           'description': data.get('description')        
       }
   )

   return jsonify(recipe)

    
