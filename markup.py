from telebot import types

adm_btn_1= types.InlineKeyboardButton(text="edit", callback_data= "edit")

add_task_btn1 = types.InlineKeyboardButton(text="Да. Сохранить и добавить", callback_data= "savee")
add_task_btn2 = types.InlineKeyboardButton(text="Нет. Редактировать", callback_data= "peredelat")



keyboard_admin = types.InlineKeyboardMarkup()
keyboard_admin.add(
    adm_btn_1,
)

keyboard_add_task = types.InlineKeyboardMarkup()
keyboard_add_task.add(
    add_task_btn1,
    add_task_btn2
)
