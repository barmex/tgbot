import configparser
from bot import keyboards
from utils import config
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

config = config.Config()



async def start(upd: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Hello I'm a bot")

async def menu(upd: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await upd.message.reply_text("Please make your choose:", reply_markup=keyboards.kbd1_reply_markup)

async def button(upd: Update, ctx: ContextTypes.DEFAULT_TYPE) -> None:
    query = upd.callback_query
    await query.answer()
    await query.edit_message_text(text=f'Selected option is: {query.data}')

if __name__ == '__main__':
    if config.token is not None:
        app = ApplicationBuilder().token(config.token).build()
        start_handler = CommandHandler('start', start)
        menu_handler = CommandHandler('menu', menu)
        app.add_handler(start_handler)
        app.add_handler(menu_handler)
        app.add_handler(CallbackQueryHandler(button))
        app.run_polling()
    else:
        logging.error('Telegram token is not set. Aborting...')
        exit(10)