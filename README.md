# Family budget API

This API allows you to create user, authorize (OAuth2) and create a budget. 

### Things not yet implemented

* Add expenses and incomes to budget.
* Share a budget with other registered users.
* Admin page.
* Add categories for incomes/expenses.
* Add tests (TDD not strong with this one).


### Stack

* Python 3.10
* FastAPI
* SQLAlchemy
* postgres

### Requirements

* Docker
* docker-compose

### Installation

1. Clone the repository

    `git clone https://github.com/michaldanielewicz/family-budget`  
  

2. Change directory to the cloned repository

    `cd family-budget`


3. Edit `.env.template` file

    ```
    POSTGRES_USER=*edit_this_value*
    POSTGRES_PASSWORD={{POSTGRES_PASSWORD}}
    ...
    ```


4. Rename `.env.template` to `.env`


5. Build the Docker image:

    `make build`


6. To run containers:

   `make up`


### Usage

Available endpoints:

    GET /users: Fetch all users (can filter by provided username)
    POST /users: Create new user
    GET /users/me: Fetch authorized user (need login)

    GET /budgets: Fetch budget (authorized user)
    POST /budgets: Create new budget

You can recall all the available endpoints and documentation at http://0.0.0.0:3030/redoc or http://0.0.0.0:3030/redoc.


### Dev

You can enter the container with app by typing `make bash`
