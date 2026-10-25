from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! My bot is online on Termux! 🚀")

if __name__ == '__main__':
    # Replace YOUR_BOT_TOKEN with the token from @BotFather
    application = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Bot is running...")
    application.run_polling()

