from telegram import KeyboardButton, ReplyKeyboardMarkup


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
