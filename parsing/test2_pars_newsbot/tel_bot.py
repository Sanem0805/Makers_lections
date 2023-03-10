import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token, user_id
import json
import datetime
from pars2 import check_news_update
# from aiogram.utils.markdown import bold, underline, code, link


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    start_buttons = ['Все новости', 'Последние 5 новостей', 'Свежие новости']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Лента новостей', reply_markup=keyboard)


@dp.message_handler(Text(equals="Все новости"))
async def get_all_news(message: types.Message):
    with open('new_dict.json') as file:
        new_dict = json.load(file)
    
    for k,v in sorted(new_dict.items()):
        # news = f"{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}\n{v['article_title']}\n{v['article_desc']}\n{v['article_url']}"
        news = f"{(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n{(v['article_title'])}\n{(v['article_title'], v['article_url'])}"      
        
        await message.answer(news)



@dp.message_handler(Text(equals="Последние 5 новостей"))
async def get_last_five_news(message: types.Message):
    with open('new_dict.json') as file:
        new_dict = json.load(file)
    
    for k,v in sorted(new_dict.items())[-5:]:
        news = f"{(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n{(v['article_title'])}\n{(v['article_title'], v['article_url'])}"      
        
        await message.answer(news)



@dp.message_handler(Text(equals="Свежие новости"))
async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()
    if len(fresh_news) >= 1:
        for k,v in sorted(fresh_news.items()):
            news = f"{(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n{(v['article_title'])}\n{(v['article_title'], v['article_url'])}"      
        
            await message.answer(news)
    else:
        await message.answer('Пока нет свежих новостей.....')

async def new_every_minute():
    while True:
        fresh_news = check_news_update()
        if len(fresh_news) >= 1:
            for k,v in sorted(fresh_news.items()):
                news = f"{(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n{(v['article_title'])}\n{(v['article_title'], v['article_url'])}"

                # get your id @userinfobot
                await bot.send_message(user_id, news, disable_notification=True)

        else:
            await bot.send_message(user_id, 'Пока нет свежих новостей....', disable_notification=True)

        await asyncio.sleep(20)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(new_every_minute())
    executor.start_polling(dp)

 # pip install aiogram