# Carhire
An example of a client/server model using a backend SQLlite database

## Initialise the database with some examples
Before the server can serve details via it's REST API, we need to create the DB.

The following will create the `carhire.db` database.
```
$ cd server
$ python db.py
Initialising database
ALL MODELS
{'id': 1, 'name': 's-max', 'manufacturer': 'Ford', 'people': 5, 'luggage': 5}
{'id': 2, 'name': 'mini', 'manufacturer': 'BMW', 'people': 4, 'luggage': 2}
ALL CARS
{'id': 1, 'registration': 'ABC 123', 'color': 'red', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5}
{'id': 2, 'registration': 'ABC 456', 'color': 'blue', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5}
{'id': 3, 'registration': 'M1N1 2', 'color': 'black', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
{'id': 4, 'registration': 'M1N1 1', 'color': 'silver', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
findByModelName
{'id': 3, 'registration': 'M1N1 2', 'color': 'black', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
{'id': 4, 'registration': 'M1N1 1', 'color': 'silver', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
ALL BOOKINGS
{'id': 1, 'customer': 'Fred Flintstone', 'start_date': '11-09-2020', 'end_date': '12-09-2020', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2, 'registration': 'M1N1 2'}
{'id': 2, 'customer': 'Wilma Flintstone', 'start_date': '13-09-2020', 'end_date': '15-09-2020', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2, 'registration': 'M1N1 2'}
{'id': 3, 'customer': 'Barney Rubble', 'start_date': '11-09-2020', 'end_date': '12-09-2020', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5, 'registration': 'ABC 123'}
{'id': 4, 'customer': 'Betty Rubble', 'start_date': '13-09-2020', 'end_date': '15-09-2020', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5, 'registration': 'ABC 123'}
findByCustomer
{'id': 1, 'customer': 'Fred Flintstone', 'start_date': '11-09-2020', 'end_date': '12-09-2020', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2, 'registration': 'M1N1 2'}
$
```
_Running this python module by itself will drop, create and fill out some default values for the database, and then run some simple queries_

## Server
The server code provides a RESTful web service for the access and manipulation of the resources associated with the carhire database.
[`server/db.py`](server/db.py) provides the core database access and control, exposing the various actions as functions within the `db` module.

### Prerequisites
`$ python -m pip install flask_restful`

This installs the python packages that the [`server/server.py`](server/server.py) code uses to provide the web service.
### usage
```
$ python server.py
 * Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://localhost:5000
Press CTRL+C to quit
```

_NB. You will need to have created the carhire.db database before running this._ (see above)

## Client
The client code provides similar functions as the db interface, but the implementation talks to the remote web service (if running) to perform the tasks rather than to a local database.

### Prerequisites
`$ python -m pip install requests`

### usage 
```
$ cd client
$ python client.py
ALL MODELS
{'id': 1, 'name': 's-max', 'manufacturer': 'Ford', 'people': 5, 'luggage': 5}
{'id': 2, 'name': 'mini', 'manufacturer': 'BMW', 'people': 4, 'luggage': 2}
ALL CARS
{'id': 1, 'registration': 'ABC 123', 'color': 'red', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5}
{'id': 2, 'registration': 'ABC 456', 'color': 'blue', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5}
{'id': 3, 'registration': 'M1N1 2', 'color': 'black', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
{'id': 4, 'registration': 'M1N1 1', 'color': 'silver', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
findByModelName
{'id': 3, 'registration': 'M1N1 2', 'color': 'black', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
{'id': 4, 'registration': 'M1N1 1', 'color': 'silver', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2}
ALL BOOKINGS
{'id': 1, 'customer': 'Fred Flintstone', 'start_date': '11-09-2020', 'end_date': '12-09-2020', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2, 'registration': 'M1N1 2'}
{'id': 2, 'customer': 'Wilma Flintstone', 'start_date': '13-09-2020', 'end_date': '15-09-2020', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2, 'registration': 'M1N1 2'}
{'id': 3, 'customer': 'Barney Rubble', 'start_date': '11-09-2020', 'end_date': '12-09-2020', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5, 'registration': 'ABC 123'}
{'id': 4, 'customer': 'Betty Rubble', 'start_date': '13-09-2020', 'end_date': '15-09-2020', 'manufacturer': 'Ford', 'model': 's-max', 'people': 5, 'luggage': 5, 'registration': 'ABC 123'}
findByCustomer
{'id': 1, 'customer': 'Fred Flintstone', 'start_date': '11-09-2020', 'end_date': '12-09-2020', 'manufacturer': 'BMW', 'model': 'mini', 'people': 4, 'luggage': 2, 'registration': 'M1N1 2'}
```
This installs the python packages that the [`client/client.py`](client/client.py) code uses to perform REST requests.

## From a Browser
You can also query the web service yourself from a browser.

### retrieve list of all models
[`http://localhost:5000/model`](http://localhost:5000/model)

### retrieve list of all cars
[`http://localhost:5000/car`](http://localhost:5000/car)

### retrieve list of all bookings
[`http://localhost:5000/booking`](http://localhost:5000/booking)

### retrieve list of all red cars (example of a REST call failure)
[`http://localhost:5000/booking?color=red`](http://localhost:5000/booking?color=red)

### find specific booking
[`http://localhost:5000/booking/3`](http://localhost:5000/booking/3)

### find all bookings of 'mini'
[`http://localhost:5000/booking?model=mini`](http://localhost:5000/booking?model=mini)

### bookings with a customer name containing 'rub'
[`http://localhost:5000/booking?customer=%rub%`](http://localhost:5000/booking?customer=%rub%)

# Simple javascript retrieval


[`http://localhost:5000/static/carhire.html`](http://localhost:5000/static/carhire.html)
