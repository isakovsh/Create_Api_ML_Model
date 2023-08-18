# Diabetes Prediction API with FastAPI

This is a README file for a Diabetes Prediction API created using FastAPI. The API utilizes a machine learning model to predict the likelihood of a person having diabetes based on input features.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Sample Requests and Responses](#sample-requests-and-responses)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Diabetes Prediction API is built using FastAPI, a modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints. The API provides a simple and efficient way to interact with the diabetes prediction model.

The machine learning model used in this API is trained on a dataset containing various health parameters such as glucose level, blood pressure, BMI, etc., and their corresponding labels indicating whether the person has diabetes or not. The model uses this information to make predictions on new data.

## Installation

To install and run the Diabetes Prediction API, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/diabetes-prediction-api.git
   ```

2. Navigate to the project directory:

   ```shell
   cd diabetes-prediction-api
   ```

3. Create a virtual environment (optional but recommended):

   ```shell
   python3 -m venv env
   source env/bin/activate  # Activate the virtual environment
   ```

4. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

5. Run the API server:

   ```shell
   uvicorn app:app --reload
   ```

   The API will be accessible at `http://localhost:8000`.

## Usage

Once the API server is up and running, you can use it to make predictions by sending HTTP requests to the provided endpoints. The API supports both JSON and form data inputs.

To interact with the API, you can use tools like cURL or Postman. Below is an example of using cURL to send a POST request with JSON data:

```shell
curl -X POST -H "Content-Type: application/json" -d '{
  "glucose": 148,
  "blood_pressure": 72,
  "bmi": 33.6,
  "age": 50
}' http://localhost:8000/predict
```

The API will respond with a JSON object containing the prediction result.

## API Endpoints

The Diabetes Prediction API provides the following endpoint:

- `POST /predict`: Accepts input data and returns the prediction result.

## Sample Requests and Responses

### Request

```shell
POST /predict
Content-Type: application/json

{
  "glucose": 148,
  "blood_pressure": 72,
  "bmi": 33.6,
  "age": 50
}
```

### Response

```json
HTTP/1.1 200 OK
Content-Type: application/json

{
  "prediction": 1,
  "probability": 0.78
}
```

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Test your changes.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
