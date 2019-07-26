# iRacing Scheduling

Application for scheduling endurance events in iracing

## Technology
* Python
    * flask
    * flask-sqlalchemy
    * flask-marshmallow
    * flask-migrate
    * marshmallow-sqlalchemy
    * psycopg2
* Docker
* Postgresql
* Adminer

## Getting started
1. Create folder in root named postgresdata
    * To store the data created by the application
2. run ``` docker-compose up ```
3. The api is now running at port 5000

## Create database schema

1. Run the application
2. run ```docker exec -it scheduling-api_schedulingapi_1 /bin/bash```
3. run ```flask db init```
4. run ```flask db migrate -m "migration message"```
5. run ```flask db upgrade```

## Update database schema 
1. Run the application
2. run ```docker exec -it scheduling-api_schedulingapi_1 /bin/bash```
4. run ```flask db migrate -m "migration message"```
5. run ```flask db upgrade```

## Front end
***__TODO__***

### Adminer
1. Navigate to localhost:8080 to access the adminer interface
2. To login:
    * System: PostgreSQL
    * Server: db
    * Username: postgres
    * Password: example
    * Database: postgres
