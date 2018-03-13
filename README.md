# Caracole.io

## Reverse Proxy

This project needs a running [traefik](https://traefik.io) instance. If you don't have one, look at those examples for
[dev](https://github.com/nim65s/traefik-dev) and [prod](https://github.com/nim65s/traefik-prod).

## Dev

Make sur caracole.local resolves to localhost, and

```
echo POSTGRES_PASSWORD=$(openssl rand -base64 32) >> .env
echo SECRET_KEY=$(openssl rand -base64 32) >> .env
echo DOMAIN_NAME=local >> .env
. .env
docker-compose up -d --build
```
