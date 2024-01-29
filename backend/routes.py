from flask import Blueprint, jsonify, request
from models import Restaurant, Pizza, RestaurantPizza, db

app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{'id': r.id, 'name': r.name, 'address': r.address} for r in restaurants])

@app_routes.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        return jsonify({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address,
            'pizzas': [{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in restaurant.pizzas]
        })
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app_routes.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'error': 'Restaurant not found'}), 404

@app_routes.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'ingredients': p.ingredients} for p in pizzas])

@app_routes.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    restaurant_id = data.get('restaurant_id')
    pizza_id = data.get('pizza_id')
    price = data.get('price')

    if not (restaurant_id and pizza_id and price):
        return jsonify({'errors': ['validation errors']}), 400

    restaurant = Restaurant.query.get(restaurant_id)
    pizza = Pizza.query.get(pizza_id)

    if not (restaurant and pizza):
        return jsonify({'errors': ['validation errors']}), 400

    restaurant_pizza = RestaurantPizza(restaurant_id=restaurant_id, pizza_id=pizza_id, price=price)
    db.session.add(restaurant_pizza)
    db.session.commit()

    return jsonify({'id': pizza.id, 'name': pizza.name, 'ingredients': pizza.ingredients})
