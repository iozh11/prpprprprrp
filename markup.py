from telebot import types

edit_notready_task_btn= types.InlineKeyboardButton(text="edit", callback_data= "edit")
do_ready_task_btn = types.InlineKeyboardButton(text="Задача выполнена", callback_data= "finished")

keyboard_for_notready_task = types.InlineKeyboardMarkup()
keyboard_for_notready_task.add(
    do_ready_task_btn,
    edit_notready_task_btn,
)


do_notready_task_btn = types.InlineKeyboardButton(text="Задача не выполнена", callback_data= "unfinished")

keyboard_for_ready_task = types.InlineKeyboardMarkup()
keyboard_for_ready_task.add(
    do_notready_task_btn,
)


add_task_btn = types.InlineKeyboardButton(text="Да. Сохранить и добавить", callback_data= "save_task")
edit_task_btn = types.InlineKeyboardButton(text="Нет. Редактировать", callback_data= "edit_task")

keyboard_add_task = types.InlineKeyboardMarkup()
keyboard_add_task.add(
    add_task_btn,
    edit_task_btn
)
