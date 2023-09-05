from telegram import Update
from telegram.ext import (
    CallbackContext,
)
import messages
import keyboards


# create a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text=messages.WELCOME_MESSAGE.format(first_name),
        parse_mode="HTML",
        reply_markup=keyboards.WELCOME_KEYBOARD,
    )


# create a function to handle the /start command
def star5(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user sends /start command

    Args:
        update (Update): updater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # get the first name of the user
    first_name = update.effective_user.first_name

    # send a message to the user
    update.message.reply_text(
        text="""Mamnun qolganingizdan xursandmiz 😊. Siz va yaqinlaringizni har doim xursand qilishga harakat qilamiz 🤗""",
        parse_mode="HTML",
        reply_markup=keyboards.WELCOME_KEYBOARD,
    )


# create a function to handle when press "ℹ️ Ma'lumot" button
def about(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user presses "ℹ️ Ma'lumot" button

    Args:
        update (Update): udpater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # send a message to the user
    update.message.reply_text(
        text="Kerakli bo'limni tanlang ⬇️",
        parse_mode="HTML",
        reply_markup=keyboards.ABOUT_KEYBOARD,
    )


# create a function to handle when press "ℹ️ Ma'lumot" button
def feedback(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user presses "ℱｍ Izoh qoldirish" button

    Args:
        update (Update): udpater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # send a message to the user
    update.message.reply_text(
        text=messages.COMMENT_MESSAGE,
        reply_markup=keyboards.FEEDBACK_KEYBOARD,
        parse_mode="HTML",
    )


def language(update: Update, context: CallbackContext) -> None:
    """this function will be called when the user presses "ℱｍ Izoh qoldirish" button

    Args:
        update (Update): udpater object that contains the update info.
        
        context (CallbackContext): context object that contains the bot info.
    """
    # send a message to the user
    update.message.reply_text(
        text="""Iltimos, tilni tanlang
Пожалуйста, выберите язык ⬇️""",
        reply_markup=keyboards.LANGUAGE_KEYBOARD,
        parse_mode="HTML",
    )