# Shopping List using FastAPI

This is a simple REST API using FastAPI you will create a simple endpoint that can use the GET and POST methods, those are the basics of REST API.

## How to install

We recommend to use virtualenv to create a virtual environment for this project and install the dependencies in the requirements.txt file, using this command:

`pip install -r requirements.txt`

## How to run

To run the project you can use the following command:

`uvicorn shopping_list:app --reload`

After that you can go to http://localhost:8000/shopping_list and you will see the items in the shopping list.

In order to try the POST method you can use Postman or cURL. 
POST using cURL:
`curl -X POST -H "Content-Type: application/json" -d '{"item":"coffee"}' http://localhost:8000/shopping_list`

Note: This is a simple example of a backend API, the frontend is not included in this project to keep it simple.


