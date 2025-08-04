## FastAPI template


### What are there in this setting?

- A FastAPI server
- A PostgresSQL database


### Running on container with docker

```bash
# docker compose up -d
```


### Running on host

```bash
$ uv venv
$ uv sync
$ uv run uvicorn app.api:app --host 0.0.0.0 --port 8000
```

