import React, { useState } from "react";
import { Link } from "react-router-dom";

import "./styles.scss";
import Form from "../../component/Form";

const inputsType = [
	{
		type: "email",
		placeholder: "Email",
		label: "Email",
		width: "100%"
	}
];

const LostPassword = () => {
	const [inputs, setInputs] = useState({
		email: ""
	});

	return (
		<div className="lost-password">
			<div className="form-container">
				<h5 className="instructions">
					Ingresa tu dirección de correo electronico y te enviaremos instrucciones para recuperar tu
					contraseña
				</h5>
				<Form
					inputsType={inputsType}
					inputs={inputs}
					setInputs={setInputs}
					buttonLabel="Enviar instrucciones"
				/>
				<Link to="/login">Cancelar</Link>
			</div>
		</div>
	);
};

export default LostPassword;
