TOKEN = 'Bot Token From BotFather'
BOT_USERNAME = '@SimplySimpleBot'

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! I am a simple bot. Type /help to see what I can do.')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a simple bot. Please type something and I will echo it back to you!')

def handle_response(test: str) -> str:
    return test

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = str(update.message.text)

    print(f'User ({update.message.chat.id}) in {message_type} sent: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Bot is running...')

    app.run_polling(poll_interval=3)
