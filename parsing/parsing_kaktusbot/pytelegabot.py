import types
from pars4 import parse_news
import telebot
from telebot import types
import json

token = '6112644611:AAHzHwat_yU37e_N2QqBjblarZdjESmP2uc'

bot = telebot.TeleBot(token)

keyboard = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('Фото')
button2 = types.KeyboardButton('Описание')
keyboard.add(button1, button2)

def read_news():
    with open('data.json') as file:
        data = json.load(file)
    return data


@bot.message_handler(commands=['start'])
def start_parse(message):
    print('!!!!!!!!!')
    bot.send_message(message.chat.id, 'Бот приветствует вас, мы начали парсить подождите пару секунд....')
    print('started')
    parse_news()
    data = read_news()
    print('data')
    for x in data:
        bot.send_message(message.chat.id, f'{x} --> *{data[x]["title"]}*', parse_mode='Markdown')
    
    message_from_bot = bot.send_message(message.chat.id, 'выберите число новости для подробной информации (1-20): ')
    bot.register_next_step_handler(message_from_bot, check_number)

def check_number(message):
    keys = [str(x) for x in range(1, 21)]
    if message.text not in keys:
        message_from_bot = bot.send_message(message.chat.id, 'Неверное число нужно выбрать число в диапазоне от(1-20): ')
        bot.register_next_step_handler(message_from_bot, check_number)
    else:
        data = read_news()
        message_from_bot = bot.send_message(message.chat.id, f'{data[message.text]["title"]}\n выберите фото или описание этой новости!', reply_markup=keyboard)
        bot.register_next_step_handler(message_from_bot, show_info, message.text, data)

def show_info(message, number, data):
    if message.text == 'Фото':
        bot.send_message(message.chat.id, data[number]['img'])
        message_from_bot = bot.send_message(message.chat.id, 'выберите число новости для подробной информации (1-20): ')
        bot.register_next_step_handler(message_from_bot, check_number)
    else:
        bot.send_message(message.chat.id, data[number]['desc'])
        message_from_bot = bot.send_message(message.chat.id, 'выберите число новости для подробной информации (1-20): ')
        bot.register_next_step_handler(message_from_bot, check_number)


bot.polling()

