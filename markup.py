from telebot import types

adm_btn_1= types.InlineKeyboardButton(text="edit", callback_data= "edit")

add_task_btn = types.InlineKeyboardButton(text="Да. Сохранить и добавить", callback_data= "save_task")
edit_task_btn = types.InlineKeyboardButton(text="Нет. Редактировать", callback_data= "edit_task")



keyboard_admin = types.InlineKeyboardMarkup()
keyboard_admin.add(
    adm_btn_1,
)

keyboard_add_task = types.InlineKeyboardMarkup()
keyboard_add_task.add(
    add_task_btn,
    edit_task_btn
)
