# SendIT-Api-V1
We are expected to create a set of API endpoints

[![Build Status](https://travis-ci.org/Bakley/SendIT-Api-V1.svg?branch=develop)](https://travis-ci.org/Bakley/SendIT-Api-V1)

[![Maintainability](https://api.codeclimate.com/v1/badges/a078df0f9b3d7e6aa7ef/maintainability)](https://codeclimate.com/github/Bakley/SendIT-Api-V1/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/a078df0f9b3d7e6aa7ef/test_coverage)](https://codeclimate.com/github/Bakley/SendIT-Api-V1/test_coverage)

## API Endpoints covered included in this branch


| Method        |       Endpoint                        |         Description                           |
| ------------- |       -------------                   |         -------------                         |
| `GET`         | `/api/v1/parcel`                      |   Gets all parcel delivery orders             |
| `GET`         | `/api/v1/parcel/<parcelid>`           |   Get a parcel delivery orders by id          |
| `POST`        | `/api/v1/parcel`                      |   Create a parcel delivery orders             |
| `GET`         | `/api/v1/user`                        |   Gets all the users                          |
| `GET`         | `/api/v1/user/<userid>`               |   Get a user by id                            |
| `POST`        | `/api/v1/users/registration`          |   Register a user                             |
| `POST`        | `/api/v1/users/login`                 |   Signin a User                               |
| `PUT`         | `/api/v1/parcels/<parcelId>/cancel`   |   Cancel the specific parcel delivery order   |


# Setting up your system

Make sure you already have Python3, Pip and Virtualenv installed in your system.

# How to get started

Start by making a directory where we will work on. Simply Open your terminal and then:

```
mkdir sentit-api-v1
```

Afterwhich we go into the directory:

```
cd sendit-api-v1
```

## Create a Python Virtual Environment for our Project

Since we are using Python 3, create a virtual environment by typing:

```
virtualenv -p python3 .
```

Before we install our project's Python requirements, we need to activate the virtual environment. You can do that by typing:

```
source bin/activate
```

## Clone and Configure a Flask Project

Login into your github account and open the project folder then follow the instruction on how to clone the existing project. It should be something similar to:

```
git clone https://github.com/Bakley/SendIT-Api-V1.git
```

Next, install the requirements by typing:

```
pip install -r requirements.txt
```

## Unit Testing
To test the endpointsensure that the following tools are available the follow steps below
   ### Tools:
     Postman
     
### Commands
  The application was tested using `nose` and coverage. To run the tests on the bash terminal use
     
     nosetests --with-coverage --cover-package=app  && coverage report
