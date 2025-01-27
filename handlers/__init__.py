from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery
from functools import partial

from handlers.start import start_command
from handlers.commands import admin_command
from handlers.callback import Anime,Manga,Category,add_category,rem_category,category,random_anime,random_manga,new_anime_series,add_series,delete_series,new_manga_series,add_manga_series,delete_manga_series,all_anime_series_msg,all_manga_series_msg,searched_anime,anime_video,manga_file,searched_manga
from handlers.message import Main_menu,new_anime_series_msg,add_series_msg,delete_series_msg,new_manga_series_msg,add_manga_series_msg,delete_manga_series_msg,main_menu,search_anime,add_category_msg,rem_category_msg
from keyboards.reply import reply_messages_list
from utils import anime,manga

def register_handlers(dp: Dispatcher):
    dp.message(CommandStart())(start_command)
    dp.message(Command("admin"))(admin_command)
    dp.message(lambda m: m.text in reply_messages_list)(main_menu)
    dp.message(Main_menu.waiting_for_anime_name)(search_anime)
    dp.message(Anime.waiting_for_name)(new_anime_series_msg)
    dp.message(Anime.waiting_for_video)(add_series_msg)
    dp.message(Anime.waiting_for_anime_id)(delete_series_msg)
    dp.message(Manga.waiting_for_name)(new_manga_series_msg)
    dp.message(Manga.waiting_for_file)(add_manga_series_msg)
    dp.message(Manga.waiting_for_file_id)(delete_manga_series_msg)
    dp.message(Category.waiting_for_amsg)(add_category_msg)
    dp.message(Category.waiting_for_rmsg)(rem_category_msg)
    dp.callback_query(lambda c: c.data == "admin_btn1")(new_anime_series)
    dp.callback_query(lambda c: c.data == "admin_btn2")(add_series)
    dp.callback_query(lambda c: c.data == "admin_btn3")(delete_series)
    dp.callback_query(lambda c: c.data == "admin_btn4")(new_manga_series)
    dp.callback_query(lambda c: c.data == "admin_btn5")(add_manga_series)
    dp.callback_query(lambda c: c.data == "admin_btn6")(delete_manga_series)
    dp.callback_query(lambda c: c.data == "admin_btn8")(all_anime_series_msg)
    dp.callback_query(lambda c: c.data == "admin_btn7")(all_manga_series_msg)
    dp.callback_query(lambda c: c.data == "random_anime")(random_anime)
    dp.callback_query(lambda c: c.data == "random_manga")(random_manga)
    dp.callback_query(lambda c: c.data == "category")(category)
    dp.callback_query(lambda c: c.data == "add_category")(add_category)
    dp.callback_query(lambda c: c.data == "rem_category")(rem_category)
    dp.callback_query(lambda c: c.data == "anime_category")()
    dp.callback_query(lambda c: c.data == "manga_category")()

    for id in anime.get_all_anime_names().values():
        dp.callback_query(lambda c, id=id: c.data == f"anime_{id}")(partial(searched_anime, id=id))
    for id in manga.get_all_manga_names().values():
        dp.callback_query(lambda c, id=id: c.data == f"manga_{id}")(partial(searched_manga, id=id))
    
    for anime_id,series_id in anime.get_anime_series_id():
        dp.callback_query(lambda c, anime_id=anime_id,series_id=series_id: c.data == f"anime_{anime_id}_{series_id}")(partial(anime_video, anime_id=anime_id,series_id=series_id))
    for manga_id,series_id in manga.get_manga_series_id():
        dp.callback_query(lambda c, manga_id=manga_id,series_id=series_id: c.data == f"manga_{manga_id}_{series_id}")(partial(manga_file, manga_id=manga_id,series_id=series_id))