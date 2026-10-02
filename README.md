# Intercessory Bot

Skeleton Telegram bot for intercessory prayer requests.
Polling-based, systemd-managed. Token lives in `.env` (untracked).

## Setup

```bash
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
cp .env.example .env   # then put the real token in
```

## Run

```bash
./venv/bin/python3 bot.py
```

## Install as a system service (user-level)

```bash
systemctl --user enable --now $HOME/.config/systemd/user/intercessory-bot.service
```

## Project layout

```
bot.py                # entrypoint: /start, /help, echo-anything stub
skeleton.py           # shared scaffolding (token load, bot build)
.env                  # LAUNDRY-style secrets, untracked
.env.example          # template
requirements.txt      # pinned deps
```