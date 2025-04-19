start "Telegram Bot" cmd /k python main.py
start "HTTP Server" cmd /k python -m http.server 5555

start "" "http://localhost:5555"