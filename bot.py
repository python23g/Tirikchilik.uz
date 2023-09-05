from dotenv import load_dotenv
import os

from telegram.ext import (
    Updater, 
    Dispatcher,
    CommandHandler,
    MessageHandler,
    Filters,
)

from handlers import (
    start,
    about,
    feedback,
    star5,
    language,
)


# getting the token from .env file
load_dotenv()
TOKEN = os.getenv("TOKEN")

# create updater object
updater: Updater = Updater(token=TOKEN)

# create dispatcher object
dispatcher: Dispatcher = updater.dispatcher


# create main function
def main():
    # add the handlers
    dispatcher.add_handler(handler=CommandHandler(command="start", callback=start))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("😊Menga hamma narsa yoqdi, 5 ❤️"), callback=star5))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("ℹ️ Ma'lumot"), callback=about))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("✍️ Izoh qoldirish"), callback=feedback))
    dispatcher.add_handler(handler=MessageHandler(filters=Filters.text("🌐 Tilni tanlash"), callback=language))

    # start the bot
    updater.start_polling()
    updater.idle()


# run the main function
if __name__ == "__main__":
    main()
