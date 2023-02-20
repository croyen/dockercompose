# dockercompose

Tutorial to build a docker image that host HTTP server for flask app with postgres and gunicorn:
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

# Build Image and run container

## Development
```
$ docker compose -f "docker-compose.dev.yml" up -d --build
```

## Production

```
$ docker compose -f "docker-compose.yml" up -d --build
$ docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
```

# Navigate to web

Development:
  http://localhost:5001/
 
Production:
  http://localhost:1337/
