# Glovo Delivery System

## Requirements

- Docker Desktop installed and running
- PowerShell opened in the project folder (the folder containing `docker-compose.yml`)

## Start the website

```powershell
docker compose up -d
```

Open <http://localhost:5000> in your browser. The first start installs Flask in the container. To view the server output:

```powershell
docker compose logs -f app
```

Press `Ctrl+C` to stop following logs. The container keeps running in the background.

## Restart after code changes

The project folder is mounted into the container, so saved Python changes appear there immediately. Restart the app to load them:

```powershell
docker compose restart app
```

If you changed `docker-compose.yml`, recreate the container:

```powershell
docker compose up -d --force-recreate app
```

Stop the app:

```powershell
docker compose down
```

## Run the command-line app

```powershell
docker compose run --rm app python main.py
```

## Check Python syntax

```powershell
docker compose run --rm --no-deps --entrypoint python app -m compileall -q .
```
