from typing import Awaitable, Callable, Dict
from telegram import Update
from telegram.ext import ContextTypes

from logger import logger

from .start_handler import setup_start_handler
from .chat_handler import setup_hr_chat_handler

all_handlers = [
    setup_start_handler,
    setup_hr_chat_handler,
]

def setup_all_handlers(app):
    for handler_setup in all_handlers:
        handler_setup(app)

