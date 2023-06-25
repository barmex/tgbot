from telegram import InlineKeyboardButton, InlineKeyboardMarkup

kbd1 = [
    [
        InlineKeyboardButton("Option1", callback_data=1),
        InlineKeyboardButton("Option2", callback_data=2)
    ],
    [InlineKeyboardButton("Option3", callback_data=3)]
]

kbd1_reply_markup = InlineKeyboardMarkup(kbd1)
