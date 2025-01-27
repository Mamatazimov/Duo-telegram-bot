from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def start_kb():
    button1 = KeyboardButton(text='Izlash 🔍')
    button2 = KeyboardButton(text='Kategoriyalar 📚')
    button3 = KeyboardButton(text='Tasodifiy 🎲')
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[button1],[button2,button3]],
        resize_keyboard=True)

    return keyboard


reply_messages_list = [
    'Izlash 🔍','Kategoriyalar 📚','Tasodifiy 🎲'
]

