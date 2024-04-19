import asyncio 
 
from aiogram import Bot, Dispatcher, Router , F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup,  CallbackQuery
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
    markup = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='привет')]]) 
    await msg.answer(text="Привет", reply_markup=markup) 


    inline_markup = InlineKeyboardMarkup(inline_keyboard = [
        [
            InlineKeyboardButton(text='Карина', callback_data='1'),
            InlineKeyboardButton(text='Юля', callback_data='2')],
        [
            InlineKeyboardButton(text='Олеся', callback_data='3')]
    ])
    await msg.answer(text="Привет", reply_markup=inline_markup) 
 


@router.callback_query(F.data == "1")
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text="разработчик")


@router.callback_query(F.data == "2")
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text="тестировщик")


@router.callback_query(F.data == "3")
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text="тимлид")

@router.callback_query()
async def callback_query_handler(callback_query: CallbackQuery):
    await callback_query.message.answer(text=callback_query.data)

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