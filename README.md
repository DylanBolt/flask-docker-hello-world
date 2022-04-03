### Flask Hello-World Lab

In this lab I will create a flask app to contain three **routes**:

1 .A `GET` ping-pong route
2. A `GET` route that reverses a random work from [this random word API](https://random-word-api.herokuapp.com/word?number=1)
3. A `POST` route that counts the length of a string

## Docker Container Creation

1. First, let's create a `Dockerfile` which specifies the build for our Flask docker image.

- We will use python version 3.9.12 by specifying `FROM python:3.9.12`
- Make sure to `COPY` the local `requirements.txt` by using `./` before `pip install`ing it
- Set environment variables like `ENV FLASK_APP=app.py` and `FLASK_RUN_HOST=0.0.0.0`
  - Setting the host to `0.0.0.0` binds to all interfaces
- Set a `CMD` to run the flask app: `CMD ["flask", "run"]`
- Specify the working directory with `WORKDIR /usr/src/app`

2. Create a `requirements.txt` file that includes Flask version 2.0.3 along with the requests package version 2.27.1

3. Create `docker-compose.yml` to easily build our container

- Put a `.` under `build` to make docker look for our local `Dockerfile`
- When publishing container to a port, the syntax is `host port:container port`
- To mount the current directory (`/usr/src/app`), specify it under the `volumes` header
- Set flask to `development` mode
- **Indentation is key**

# Docker-compose Commands:

To run the container:
```
docker-compose up

```
