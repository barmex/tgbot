import configparser
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

config = configparser.ConfigParser()
config.read('config.ini')
token = config['tgbot']['token']



async def start(upd: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await ctx.bot.send_message(chat_id=upd.effective_chat.id, text="Hello I'm a bot")

if __name__ == '__main__':
    app = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)
    app.run_polling()