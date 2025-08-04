# Marina SAT Solver API

This repo exposes Marina, a SAT solver written in OCaml, through an HTTPS API using Docker and deployed on Render.

## What it does

- Wraps the Marina SAT solver with a REST API
- Containerized with Docker for easy deployment
- Deployed on Render with HTTPS support

## Usage

```bash
# Build and run locally
docker build -t marina-api .
docker run -p 5000:5000 marina-api
```

## API

```http
POST /api/marina
Content-Type: application/json

{
  "proposition": "<your proposition here>"
}
```

Returns:
```json
{
  "result" : "(<your proposition>, <true or false>)"
}
```

## Live API

https://marina-api-hmc8.onrender.com/api/marina