from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


WELCOME_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🔥 Mahsulotlar"),
            KeyboardButton(text="📥 Savat"),
        ],
        [
            KeyboardButton(text="💼 Hamkorlik"),
            KeyboardButton(text="ℹ️ Ma'lumot"),
        ],
        [
            KeyboardButton(text="🌐 Tilni tanlash"),
        ]
    ]
    ,
    resize_keyboard=True,
)


ABOUT_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Izoh qoldirish"),
        ],
        [
            KeyboardButton(text="🚀 Yetkazib berish shartlari"),
            KeyboardButton(text="☎️ Kontaktlar"),
        ],
        [
            KeyboardButton(text="🏠 Bosh menyu"),
        ]
    ],
    resize_keyboard=True,
)

FEEDBACK_KEYBOARD = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="😊Menga hamma narsa yoqdi, 5 ❤️"),
        ],
        [
            KeyboardButton(text="☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️"),
        ]
    ],
    resizable_keyboard=True,
)

LANGUAGE_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="UZ", callback_data="uz"),
        ],
        [
            InlineKeyboardButton(text="RU", callback_data="ru"),
        ]
    ]
)