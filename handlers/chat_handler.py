from logger import logger
from telegram import Update
from telegram.ext import ContextTypes, MessageHandler, filters
from utils.message_utils import  send_message
import aiohttp
from config import API_HOST

async def handle_hr_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message:
        await send_message(update, context, "Пожалуйста введите вопрос")
        return
    
    message = update.message.text

    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{API_HOST}/generate", 
            json={"message": message}  # Send the message as JSON body
        ) as resp:
            result = await resp.json()
            # Extract only the part after "### Ответ:\n"
            full_response = result["response"]
            answer = full_response.strip()
            await send_message(update, context, text=answer)

# Setup the photo receipt handlers in the application
def setup_hr_chat_handler(application):
    application.add_handler(MessageHandler(
        filters.ALL & ~filters.COMMAND, 
        handle_hr_chat
    ))

    logger.debug("Добавлены обработчик вопросов о LATOKEN и хакатоне")


