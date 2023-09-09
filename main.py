import telebot
import markup

import os
from dotenv import load_dotenv

from texts import startt, add_taskk

import workwithDatabase

datebase = workwithDatabase.Datebase()

load_dotenv()
api_token = os.getenv('TELEGRAM_API_TOKEN')
bot = telebot.TeleBot(api_token)



# команды
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, startt)




@bot.message_handler(commands=['all_tasks'])
def all_task(message):
    number_of_tasks = datebase.select_all_task()
    for task in number_of_tasks:
            text = f"номер: {task[0]}, задача: {task[1]}, дата: {task[2]}"
            bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['all_notready_tasks'])
def all_notready_tasks(message):
    number_of_tasks = datebase.select_notready_task()
    if not number_of_tasks:
        bot.send_message(message.chat.id, 'Вы выполнили все задачи')
    for task in number_of_tasks:
            text = f"номер: {task[0]}, задача: {task[1]}, дата: {task[2]}"
            bot.send_message(message.chat.id, text, reply_markup=markup.keyboard_for_notready_task)



@bot.message_handler(commands=['all_ready_tasks'])
def all_ready_tasks(message):
    number_of_tasks = datebase.select_ready_task()
    if not number_of_tasks:
        bot.send_message(message.chat.id, "Нет выполненных задач")
    for task in number_of_tasks:
            text = f"номер: {task[0]}, задача: {task[1]}, дата: {task[2]}"
            bot.send_message(message.chat.id, text, reply_markup=markup.keyboard_for_ready_task)



@bot.message_handler(commands=['add_task'])
def add_task(message):
    bot.send_message(message.chat.id, add_taskk)

    name = bot.register_next_step_handler(message, name_task)



def name_task(message):
    global name

    name = message.text

    if datebase.select_task(name) is None:
        bot.send_message(message.chat.id, f"Задача: \"{name}\"?", reply_markup=markup.keyboard_add_task)
        
    else:
        bot.send_message(message.chat.id, "Такая задача уже существует")



@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global name
    if call.data == "save_task":
        datebase.add_task(name, 28, ready=0)
        bot.send_message(call.message.chat.id, "Задача была добавлена")
    if call.data == "edit_task":
        bot.send_message(call.message.chat.id, 'Введите задачу заново') 
        name = bot.register_next_step_handler(call.message, name_task)





    
bot.polling()