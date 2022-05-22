import React, { useState } from 'react'
import axios from 'axios';

const App = () => {

	const [carPlate, setCarPlate] = useState('');
	const [responseStatus, setResponseStatus] = useState({});

	const handleInputChange = (e) => {
		/**
	 	* Handle input of the input text field.
		* When there is a search active and function is activated, clear out the old search.
		*/
		e.preventDefault();
		setCarPlate(e.target.value);
		if (responseStatus)
			setResponseStatus({});
	}

	const handleSubmit = () => {
		/**
	 	* Call api to get the car name from a car plate.
		* Depending on the api response, set a state of success, warning or error message.
		*/
		const car_plate = carPlate.trim().toLocaleLowerCase();
		const url = `http://localhost:8000/api/${car_plate}/`;
		axios.get(url)
			.then(res => {
				const message = `The name for the car plate ${carPlate} is ${res.data.name}.`;
				setResponseStatus({type: "success", message: message});
			})
			.catch(error => {
				if (error.response.status === 404) {
					setResponseStatus({type: "warning", message: "Could not find a car with the requested plate"});
				} else {
					setResponseStatus({type: "danger", message: "We are having some problems right now. Please try again later."});
				}
			})
	}

	return (
		<div className="container">
			<h1>Car app</h1>
			<label>Search a car name by plate</label>
			<input 
				className="form-control" 
				type="text"
				placeholder="Enter a car plate..." 
				value={ carPlate }
				onChange={ (e) => handleInputChange(e) }
			/>
			<button 
				className="btn btn-primary m-4"
				// Enable button if there is content in the input field
				disabled={ !carPlate.trim() }
				onClick={ () => handleSubmit() }
			>Submit</button>
			{
				// If there is a responseStatus (from the state), show it.
				responseStatus && 
					<div className={`alert alert-${ responseStatus.type }`} role="alert">
						{ responseStatus.message }
					</div>
			}
		</div>
	)
}

export default App;