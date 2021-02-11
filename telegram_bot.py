import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext

access_token = ""
bot = telegram.Bot(token=access_token)
updater = Updater(token=access_token, use_context=True)
dispatcher = updater.dispatcher


# noinspection PyUnusedLocal
def hello(update: telegram.Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')


updater = Updater(access_token)
updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
