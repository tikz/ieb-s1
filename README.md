# IEB (S1)

## Run
### Local
```
pip install pipenv
pipenv install
pipenv shell

ENCRYPTION_KEY=<key> python client.py <host>:<port> <product code>
```

### Ejemplo instancia Docker
```
docker run --add-host=host.docker.internal:host-gateway --env ENCRYPTION_KEY=oHFJ7Llz1EI6MP478jrhHLJJFOmnvvHxoGOPxVR7oUM= ghcr.io/tikz/ieb-s1:main host.docker.internal:1234 F600-L-X
```