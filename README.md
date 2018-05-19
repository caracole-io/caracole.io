# Caracole.io

## Development

### Install Dependencies

*you should work in a virtualenv with python3.6*

```
pip3 install -U -r requirements.txt
```

### Create an sqlite DB

```
./manage.py migrate
```

### Run the development server

```
./manage.py runserver
```

And go on http://localhost:8000

## Integration

### Reverse Proxy

This project needs a running [traefik](https://traefik.io) instance.
You can use https://github.com/nim65s/traefik-dev.

### Configuratoin

Make sure `caracole.local` resolves to `localhost`, and:

```
echo POSTGRES_PASSWORD=$(openssl rand -base64 32) >> .env
echo SECRET_KEY=$(openssl rand -base64 32) >> .env
echo EMAIL_HOST_PASSWORD="the real smtp password" >> .env
echo DOMAIN_NAME=local >> .env
echo DEBUG=True >> .env
. .env
```

### Launch

```
docker-compose up -d --build
```

And go on http://caracole.local

You may then want to create an admin: `docker-compose exec app ./manage.py createsuperuser`

## Production

Same as Integration, but with with https://github.com/nim65s/traefik-prod, a proper `DOMAIN_NAME`, and not `DEBUG=True`
