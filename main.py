import telebot
import markup

import os
from dotenv import load_dotenv

from texts import startt, add_taskk

import db1

datebase = db1.Datebase()

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
    # print(number_of_tasks)
    for task in number_of_tasks:
            text = f"номер: {task[0]}, задача: {task[1]}, дата: {task[2]}"
            bot.send_message(message.chat.id, text)



@bot.message_handler(commands=['all_notready_tasks'])
def all_notready_tasks(message):
    number_of_tasks = datebase.select_notready_task()
    if number_of_tasks:
        pass
    else:
        bot.send_message(message.chat.id, 'Вы выполнили все задачи')
    for task in number_of_tasks:
            text = f"номер: {task[0]}, задача: {task[1]}, дата: {task[2]}"
            bot.send_message(message.chat.id, text, reply_markup=markup.keyboard_admin)



@bot.message_handler(commands=['all_ready_tasks'])
def all_ready_tasks(message):
    number_of_tasks = datebase.select_ready_task()
    if number_of_tasks:
        pass
    else:
        bot.send_message(message.chat.id, "Нет выполненных задач")
    for task in number_of_tasks:
            text = f"номер: {task[0]}, задача: {task[1]}, дата: {task[2]}"
            bot.send_message(message.chat.id, text, reply_markup=markup.keyboard_admin)



@bot.message_handler(commands=['add_task'])
def add_task(message):
    bot.send_message(message.chat.id, add_taskk)

    name = bot.register_next_step_handler(message, name_task)



def name_task(message):
    name = message.text

    if datebase.select_task(name) is None:
        pass
    else:
        bot.send_message(message.chat.id, "Такая задача уже существует")
        return
    
    bot.send_message(message.chat.id, f"Задача:{name}?", reply_markup=markup.keyboard_add_task)
    datebase.add_task(name, 28, ready=0)


bot.polling()