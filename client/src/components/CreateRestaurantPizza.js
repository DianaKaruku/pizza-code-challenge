// CreateRestaurantPizza.js

import React, { useState } from 'react';
import axios from 'axios';

function CreateRestaurantPizza() {
  const [price, setPrice] = useState('');
  const [pizzaId, setPizzaId] = useState('');
  const [restaurantId, setRestaurantId] = useState('');
  const [errors, setErrors] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    const data = {
      price: parseFloat(price),
      pizza_id: parseInt(pizzaId, 10),
      restaurant_id: parseInt(restaurantId, 10),
    };

    axios.post('/restaurant_pizzas', data)
      .then(response => console.log(response.data))
      .catch(error => setErrors(error.response.data.errors));
  };

  return (
    <div>
      <h1>Create Restaurant Pizza</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Price:
          <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} />
        </label>
        <br />
        <label>
          Pizza ID:
          <input type="number" value={pizzaId} onChange={(e) => setPizzaId(e.target.value)} />
        </label>
        <br />
        <label>
          Restaurant ID:
          <input type="number" value={restaurantId} onChange={(e) => setRestaurantId(e.target.value)} />
        </label>
        <br />
        <button type="submit">Create Restaurant Pizza</button>
      </form>
      {errors && <p>Error: {errors.join(', ')}</p>}
    </div>
  );
}

export default CreateRestaurantPizza;
