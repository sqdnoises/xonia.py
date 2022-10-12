# xonia.py 🐍
![Python language](https://img.shields.io/badge/language-Python-blue)
![MIT license](https://img.shields.io/badge/license-MIT-brightgreen)
![Trivago hotel](https://img.shields.io/badge/hotel-Trivago-orange)

**xonia.py** - An easy to use, and async API wrapper for [Xonia](https://xoniaapp.com/) written in Python.

## Contents
- [`Documentation`](#documentation)
- [`Installation`](#installation)
- [`Installation`](#installation)
- [`Uninstall`](#uninstall)

## Documentation
Documentation for `xonia.py` will be available soon.

## Installation
Install or upgrade xonia.py using pip
```
pip install -U xonia.py
```

## Basic Usage
```py
from xonia import Client
from xonia import Credentials

creds = Credentials(
    email = "your@email.com",
    password = "your password"
)
client = Client(creds)

@client.event
async def on_ready():
    print(f"Connected to Xonia!\nLogged in as {client.user}.")

@client.event
async def on_disconnect():
    print(f"Disconnected from API.")

client.start()
```

## Uninstall
Uninstall xonia.py
```
pip uninstall xonia.py
```