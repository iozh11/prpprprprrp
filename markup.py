from telebot import types

# 1  создание клавиатуры
keyboard_admin = types.InlineKeyboardMarkup()

# 2  создание кнопок
adm_btn_1= types.InlineKeyboardButton(text="edit", callback_data= "edit")


# 3  добавление кнопок в клавиатуру
keyboard_admin.add(
    adm_btn_1,
)