# datkombot

Telegram Bot, which replies "und Sicherheit!" to a message containing "Datenkommunikation" without "und Sicherheit".

## Building

Install dependencies and start application

> Make sure to export your bot token using `export BOT_TOKEN=...` on your shell! The bot cannot perform anything without a valid token!

```
pip install -r requirements.txt

python3 datkombot.py
```

## Using with Docker

Run the image using

```
docker run -e BOT_TOKEN=... ghcr.io/gameheld/datkombot:latest
```

## Using Kubernetes

Deploy the YAML inside `./deploy/` to your cluster:

```
kubectl create -f ./deploy/bot.yaml
```