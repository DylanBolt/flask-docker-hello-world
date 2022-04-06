# Flask Hello-World Lab

In this lab I will create a flask app to contain three **routes**:

1. A `GET` ping-pong route
2. A `GET` route that reverses a random work from [this random word API](https://random-word-api.herokuapp.com/word?number=1)
3. A `POST` route that counts the length of a string


## Docker-compose Commands:

To run the container:
```
docker-compose up
```
To run the make-request.py file from within the docker container:
```
docker-compose exec web python make-request.py
```
