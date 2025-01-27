from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import anime,manga

# Admin keyboard 
admin = InlineKeyboardBuilder()
admin.row(
    InlineKeyboardButton(text='Yangi anime seria yaratish', callback_data='admin_btn1'),
    InlineKeyboardButton(text='Serialarni yuklash', callback_data='admin_btn2'),
    InlineKeyboardButton(text='Serialarni o\'chirish', callback_data='admin_btn3'),
    InlineKeyboardButton(text='Yangi manga seria yaratish', callback_data='admin_btn4'),
    InlineKeyboardButton(text='Qismlarni yuklash', callback_data='admin_btn5'),
    InlineKeyboardButton(text='Qismlarni o\'chirish', callback_data='admin_btn6'),

)
admin.adjust(3)
admin.row(InlineKeyboardButton(text="Barcha manga", callback_data='admin_btn7'),
          InlineKeyboardButton(text="Barcha anime", callback_data='admin_btn8'))
admin.row(InlineKeyboardButton(text="Kategoriya", callback_data='category'))
admin_kb = admin.as_markup()

def admin_category_kb():
    category = InlineKeyboardBuilder()
    category.row(InlineKeyboardButton(text="Qo'shish", callback_data="add_category"),
                 InlineKeyboardButton(text="O'chirish", callback_data="rem_category"))
    category = category.as_markup()
    return category

# search keyboard
def search_kb(name):
    search = InlineKeyboardBuilder()
    all_anime = anime.searching_anime(name)
    all_manga = manga.searching_manga(name)
    for id,name in all_anime:
        name = name.capitalize()
        search.row(InlineKeyboardButton(text=name, callback_data=f'anime_{id}'))
    for id,name in all_manga:
        name = name.capitalize()
        search.row(InlineKeyboardButton(text=name, callback_data=f'manga_{id}'))
    if len(all_anime) >= 10:
        search.adjust(2)
    else:
        search.adjust(1)
    search = search.as_markup()
    return search

def series_kb(id):
    series = InlineKeyboardBuilder()
    series_list = anime.get_anime_series(id)
    for i in series_list:
        series.row(InlineKeyboardButton(text=f"{i[1]}-qism", callback_data=f"anime_{id}_{i[1]}"))
    if len(series_list) <= 10:
        series.adjust(2)
    elif len(series_list) >= 20:
        series.adjust(4)
    else:
        series.adjust(3)
    series = series.as_markup()
    return series

def chapter_kb(id):
    chapter = InlineKeyboardBuilder()
    chapter_list = manga.get_manga_series(id)
    for i in chapter_list:
        chapter.row(InlineKeyboardButton(text=f"{i[1]}-qism", callback_data=f"manga_{id}_{i[1]}"))
    if len(chapter_list) <= 10:
        chapter.adjust(2)
    elif len(chapter_list) >= 20:
        chapter.adjust(4)
    else:
        chapter.adjust(3)
    chapter = chapter.as_markup()
    return chapter

def random_kb():
    random = InlineKeyboardBuilder()
    random.row(InlineKeyboardButton(text="Random anime", callback_data="random_anime"),
               InlineKeyboardButton(text="Random manga", callback_data="random_manga"))
    random = random.as_markup()
    return random

def category_kb():
    category = InlineKeyboardBuilder()
    category.row(InlineKeyboardButton(text="Anime", callback_data="anime_category"),
                 InlineKeyboardButton(text="Manga", callback_data="manga_category"))
    category = category.as_markup()
    return category






