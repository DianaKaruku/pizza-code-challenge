from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizzarestaurants.db'
db = SQLAlchemy(app)

# Models
class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = relationship('Pizza', secondary='restaurant_pizza')

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, ForeignKey('pizza.id'), nullable=False)

# Validations
@db.event.listens_for(RestaurantPizza.price, 'set', retval=True)
def validate_price(target, value, oldvalue, initiator):
    if not (1 <= value <= 30):
        raise ValueError("Price must be between 1 and 30.")

# Routes
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([{"id": r.id, "name": r.name, "address": r.address} for r in restaurants])

@app.route('/restaurants/<int:restaurant_id>', methods=['GET'])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        pizzas = [{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in restaurant.pizzas]
        return jsonify({"id": restaurant.id, "name": restaurant.name, "address": restaurant.address, "pizzas": pizzas})
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/restaurants/<int:restaurant_id>', methods=['DELETE'])
def delete_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    if restaurant:
        # Delete associated RestaurantPizzas
        RestaurantPizza.query.filter_by(restaurant_id=restaurant_id).delete()
        # Delete the Restaurant
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([{"id": p.id, "name": p.name, "ingredients": p.ingredients} for p in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    try:
        new_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_pizza)
        db.session.commit()
        return jsonify({"id": new_pizza.id, "name": new_pizza.pizza.name, "ingredients": new_pizza.pizza.ingredients})
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)