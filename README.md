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

Inside the namespace you want to deploy to, run

```bash
export BOT_TOKEN=...

kubectl create secret generic datkombot-token --from-literal=BOT_TOKEN=$BOT_TOKEN
```

to create a Secret resource for the bot token. Then, deploy the YAML inside `./deploy/` to your cluster!

```
kubectl create -f ./deploy/bot.yaml
```

> Note that if you omit creating the secret, the deployment will not start due to the unavailability of the required resource.
> If you'd like to change this behavior, set `optional: true` in the `envFrom` secretRef in `./deploy/bot.yaml`.