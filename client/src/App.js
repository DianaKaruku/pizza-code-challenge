import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

import RestaurantList from './components/RestaurantList';
import RestaurantDetail from './components/RestaurantDetail';
import PizzaList from './components/PizzaList';
import CreateRestaurantPizza from './components/CreateRestaurantPizza';

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/restaurants">View Restaurants</Link>
          </li>
          <li>
            <Link to="/pizzas">View Pizzas</Link>
          </li>
          <li>
            <Link to="/create-restaurant-pizza">Create Restaurant Pizza</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<RestaurantList />} />
        <Route path="/restaurants/:id" element={<RestaurantDetail />} />
        <Route path="/pizzas" element={<PizzaList />} />
        <Route path="/create-restaurant-pizza" element={<CreateRestaurantPizza />} />
      </Routes>
    </Router>
  );
}

export default App;




