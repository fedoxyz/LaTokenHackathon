from logger import logger

from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters, ConversationHandler
from utils.message_utils import send_message
from typing import Any

start_message = "Задай мне вопрос о работе в LATOKEN или хакатоне." # Сообщение пользователям
 

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> Any:
    text = start_message    

    if update.message:
        await send_message(update, context, text, parse_mode='Markdown', disable_web_page_preview=True )
    elif update.callback_query and update.effective_chat:
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
        )
        
    return ConversationHandler.END 

def setup_start_handler(application):
    application.add_handler(CommandHandler("start", start_handler))
    logger.debug("Start handlers added");
