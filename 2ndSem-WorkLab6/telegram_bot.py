import logging
from telegram.ext import CommandHandler, MessageHandler, filters, Application

logging.basicConfig(level = logging.INFO)

TOKEN = '7561355539:AAEgsXY7aHkShNfDEYJvA1UqYPVHFIVKFqU'


async def start(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = 'Привет! Я повторю любое твое сообщение, как эхо.')

async def echo(update, context):
    await context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

def main():
    aplication = Application.builder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT, echo)

    aplication.add_handler(start_handler)
    aplication.add_handler(echo_handler)


    aplication.run_polling()

if __name__ == '__main__':
    main()