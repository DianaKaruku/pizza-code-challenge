import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
    const [restaurants, setRestaurants] = useState([]);

    useEffect(() => {
        
        axios.get('http://localhost:5000/restaurants')
            .then(response => setRestaurants(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div>
            <h1>Restaurant List</h1>
            <ul>
                {restaurants.map(restaurant => (
                    <li key={restaurant.id}>
                        <h2>{restaurant.name}</h2>
                        <p>{restaurant.address}</p>
                        
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;

