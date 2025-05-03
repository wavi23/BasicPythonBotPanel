# Simple Discord Bot Panel in Discord.PY

## `📁` Project Structure

```
|-- bot
| |-- cogs/ # Moduły/cogi bota
| |-- config.py # Ustawienia bota (TOKEN, CHANNEL_ID itd.)
| |-- main.py # Główna logika bota
|-- web
| |-- app.py # Panel webowy (Flask)
| |-- config.py # (opcjonalny) config do panelu
| |-- static/
| | |-- css/index.css # Style CSS
| | |-- js/ # (opcjonalnie) skrypty JS
| |-- templates/index.html # Szablon HTML
```

---

## `🚀` Start Project

### 1. Install requirements

```bash
pip install -r requirements.txt
```

### 2. Config.py

```py
TOKEN = "" # Your bot token
```