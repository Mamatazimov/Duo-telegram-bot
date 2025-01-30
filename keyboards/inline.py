from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from utils import anime,manga
from config import category_list
# Admin keyboard 
admin = InlineKeyboardBuilder()
admin.row(
    InlineKeyboardButton(text='Yangi anime seria yaratish', callback_data='admin_btn1'),
    InlineKeyboardButton(text='Serialarni yuklash', callback_data='admin_btn2'),
    InlineKeyboardButton(text='Serialarni o\'chirish', callback_data='admin_btn3'),
    InlineKeyboardButton(text='Animega nomlar qo\'shish', callback_data='admin_btn_o1'),
    InlineKeyboardButton(text='Yangi manga seria yaratish', callback_data='admin_btn4'),
    InlineKeyboardButton(text='Qismlarni yuklash', callback_data='admin_btn5'),
    InlineKeyboardButton(text='Qismlarni o\'chirish', callback_data='admin_btn6'),
    InlineKeyboardButton(text='Mangaga nomlar qo\'shish', callback_data='admin_btn_o2'),

)
admin.adjust(4)
admin.row(InlineKeyboardButton(text="Barcha manga", callback_data='admin_btn7'),
          InlineKeyboardButton(text="Barcha anime", callback_data='admin_btn8'))
admin.row(InlineKeyboardButton(text="Kategoriya", callback_data='category'),
          InlineKeyboardButton(text="Statistika", callback_data='stats'))
admin.row(InlineKeyboardButton(text="Barchaga xabar yuborish", callback_data='send_all'))
admin_kb = admin.as_markup()

def admin_category_kb():
    category = InlineKeyboardBuilder()
    category.row(InlineKeyboardButton(text="Qo'shish", callback_data="add_category"),
                 InlineKeyboardButton(text="O'chirish", callback_data="rem_category"))
    category = category.as_markup()
    return category

def search_kb(name):
    search = InlineKeyboardBuilder()
    all_anime = anime.searching_anime(name)
    all_manga = manga.searching_manga(name)
    for id,name,category,o_name in all_anime:
        name = name.capitalize()
        search.row(InlineKeyboardButton(text=name, callback_data=f'anime_{id}'))
    for id,name,category,o_name in all_manga:
        name = name.capitalize()
        search.row(InlineKeyboardButton(text=name, callback_data=f'manga_{id}'))
    if len(all_anime) >= 10:
        search.adjust(2)
    else:
        search.adjust(1)
    search = search.as_markup()
    return search

def series_kb(id,current_page):
    series = InlineKeyboardBuilder()
    series_list = anime.get_anime_series(id)
    series_list_len = len(series_list)
    keyboard_pages_num = series_list_len / 16
    keyboard_pages_num +=1 if series_list_len % 16 != 0 else 0
    start_index = (int(current_page) - 1) * 16
    end_index = start_index + 16
    items = series_list[start_index:end_index]
    if int(current_page) > int(keyboard_pages_num//1) or int(current_page) <= 0:
        return 1
    else:
        for i in items:
            series.row(InlineKeyboardButton(text=f"{i[1]}-qism", callback_data=f"animeid_{id}_{i[1]}"))
        series.adjust(4)
        series.row(InlineKeyboardButton(text="Orqaga", callback_data=f"animepage_{int(current_page)-1}_{id}"),
                InlineKeyboardButton(text=f"{current_page}/{int(keyboard_pages_num//1)}", callback_data=f"just_for_info"),
                InlineKeyboardButton(text="Keyingi", callback_data=f"animepage_{int(current_page)+1}_{id}"))
        series = series.as_markup()
        return series

def chapter_kb(id,current_page):
    chapter = InlineKeyboardBuilder()
    chapter_list = manga.get_manga_series(id)
    series_list_len = len(chapter_list)
    keyboard_pages_num = series_list_len / 16
    keyboard_pages_num +=1 if series_list_len % 16 != 0 else 0
    start_index = (int(current_page) - 1) * 16
    end_index = start_index + 16
    items = chapter_list[start_index:end_index]
    if int(current_page) > int(keyboard_pages_num//1) or int(current_page) <= 0:
        return 1
    else:  
        for i in items:
            chapter.row(InlineKeyboardButton(text=f"{i[1]}-qism", callback_data=f"mangaid_{id}_{i[1]}"))
        chapter.adjust(4)
        chapter.row(InlineKeyboardButton(text="Orqaga", callback_data=f"mangapage_{int(current_page)-1}_{id}"),
                InlineKeyboardButton(text=f"{current_page}/{int(keyboard_pages_num//1)}", callback_data=f"just_for_info"),
                InlineKeyboardButton(text="Keyingi", callback_data=f"mangapage_{int(current_page)+1}_{id}"))
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

def anime_category_kb():
    category = InlineKeyboardBuilder()
    for i in category_list:
        category.row(InlineKeyboardButton(text=f"{i.capitalize()}", callback_data=i))
    category.adjust(3)
    category.row(InlineKeyboardButton(text="Bo'ldi✅", callback_data="category_done"))

    category = category.as_markup()
    return category

def search_category_kb(c_list,qiymat):
    search = InlineKeyboardBuilder()
    all_anime = c_list
    if qiymat == "anime":
        for id in all_anime:
            name = anime.get_anime_name(id)[0]
            name = name.capitalize()
            search.row(InlineKeyboardButton(text=name, callback_data=f'anime_{id}'))
    elif qiymat == "manga":
        for id in all_anime:
            name = manga.get_manga_name(id)[0]
            name = name.capitalize()
            search.row(InlineKeyboardButton(text=name, callback_data=f'manga_{id}'))
    if len(all_anime) >= 10:
        search.adjust(2)
    else:
        search.adjust(1)
    search = search.as_markup()
    return search


