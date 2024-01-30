// RestaurantDetail.js

import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function RestaurantDetail() {
  const [restaurant, setRestaurant] = useState(null);
  const { id } = useParams();

  useEffect(() => {
    axios
      .get(`http://localhost:5000/restaurants/${id}`)
      .then((response) => setRestaurant(response.data))
      .catch((error) => console.error(error));
  }, [id]);

  if (!restaurant) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h1>{restaurant.name}</h1>
      <p>{restaurant.address}</p>
     
     
    </div>
  );
}

export default RestaurantDetail;
