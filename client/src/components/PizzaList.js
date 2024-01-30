import React, { useState, useEffect } from 'react';
import axios from 'axios';

function PizzaList() {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    axios
      .get('http://localhost:5000/pizzas')
      .then((response) => setPizzas(response.data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1>Pizza List</h1>
      <ul>
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            <h2>{pizza.name}</h2>
            <p>{pizza.ingredients}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default PizzaList;
