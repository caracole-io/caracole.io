# Caracole.io

## Configuration

```
echo POSTGRES_PASSWORD=$(openssl rand -base64 32) >> .env
echo SECRET_KEY=$(openssl rand -base64 32) >> .env
echo EMAIL_HOST_PASSWORD="the real smtp password" >> .env
echo DOMAIN_NAME=localhost >> .env  # not in production
echo DEBUG=True >> .env  # not in production
. .env
```

## Development

### Install Dependencies

```
pip3 install -U pipenv
pipenv install --dev
```

### Create an sqlite DB

```
./manage.py migrate
```

### Run the development server

```
./manage.py runserver
```

And go on http://caracole.localhost:8000

You may then want to create an admin: `./manage.py createsuperuser`

## Integration

### Reverse Proxy

This website needs a reverse proxy, like [proxyta.net](https://framagit.org/nim65s/proxyta.net)

### Launch

```
docker-compose up -d --build
```

And go on http://caracole.localhost

You may then want to create an admin: `docker-compose exec app ./manage.py createsuperuser`

## Production

Same as Integration, but with with the prod-le version of [proxyta.net](https://framagit.org/nim65s/proxyta.net), a
proper `DOMAIN_NAME`, and not `DEBUG=True`.
