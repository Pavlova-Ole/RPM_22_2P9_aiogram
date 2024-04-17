import asyncio 
 
from aiogram import Bot, Dispatcher, Router 
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton 
from aiogram.filters import Command  
from aiogram.types.bot_command import BotCommand 
 
bot = Bot(token="7173826357:AAFWJEthXIVu94kLaZwrQjECv2_mOjB8MPQ") 
dp = Dispatcher() 
 
router = Router() 
 
@router.message(Command("start")) 
async def start_handler(msg: Message): 
    await bot.set_my_commands([ 
        BotCommand(command='start', description='Запуск бота'), 
        BotCommand(command='set_time', description='Задать время рассылки'), 
        BotCommand(command='help', description='Справка') 
    ]) 
    await msg.answer(text="Привет") 
     
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton('привет')]]) 
    await msg.answer(text="Привет", reply_markup=markup) 
 
 
@router.message(Command("help")) 
async def start_handler(msg: Message): 
    await msg.answer(text="Крч ребята если бот лег то звонить павлОвой (+79109245056)") 
 
@router.message(Command("set_time")) 
async def start_handler(msg: Message): 
    await msg.answer(text="Выберите время в формате ЧЧ:ММ для рассылки картинок") 
 
async def main(): 
    await dp.start_polling(bot) 
 
dp.include_routers(router) 
 
if __name__ == '__main__': 
    asyncio.run(main())