import telebot
import requests
from selenium import webdriver
import time
import sqlite3


bot = telebot.TeleBot('5468702833:AAGS0zvI_rXxlYh9yOnnGDBAxYbquoDA7Q0')

# driver = webdriver.Chrome()


@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    music = telebot.types.KeyboardButton('Музыка')
    photo = telebot.types.KeyboardButton('Фото')
    end = telebot.types.KeyboardButton('Отмена')
    print("Hello world!")
    markup.add(music, photo, end)
    msg = bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!', reply_markup=markup)
    bot.register_next_step_handler(msg, search)


@bot.message_handler(content_types='text')
def search(message):
    if message.text == 'Фото':
        bot.send_photo(message.chat.id, open('sunset.jpg', 'rb'), caption='Принято')
    elif message.text == 'Музыка':
        bot.send_audio(message.chat.id, open('The_Piano_Guys_Lyceum_Philharmonic_Orchestra_Matthew_John_Nelson_Lyudvig_van_Betkhoven_-_Beethovens_5_Secrets_48078402.mp3', 'rb'), )
    elif message.text == 'Отмена':
        msg = telebot.types.ReplyKeyboardRemove()
        bot.send_photo(message.chat.id, open('bye.jpg', 'rb'), reply_markup=msg)
    else:
        bot.send_message(message.chat.id, "Выберите одно из двух: музыка или фото")


bot.polling(none_stop=True)