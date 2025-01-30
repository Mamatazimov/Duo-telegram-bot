from aiogram import Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import CallbackQuery
from functools import partial

from handlers.start import start_command
from handlers.commands import admin_command
from handlers.callback import Anime,Manga,Category,Other_name,Send_msg,searched_anime2,searched_manga2,send_all,manga_category,categorys,add_other_name,anime_category,add_category,rem_category,category,random_anime,random_manga,new_anime_series,add_series,delete_series,new_manga_series,add_manga_series,delete_manga_series,all_anime_series_msg,all_manga_series_msg,searched_anime,anime_video,manga_file,searched_manga
from handlers.message import Main_menu,send_msg_to_all,add_other_name_msg,new_anime_series_msg,add_series_msg,delete_series_msg,new_manga_series_msg,add_manga_series_msg,delete_manga_series_msg,main_menu,search_anime,add_category_msg,rem_category_msg
from keyboards.reply import reply_messages_list
from utils import anime,manga
from config import category_list


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
    dp.message(Other_name.waiting_for_names)(add_other_name_msg)
    dp.message(Send_msg.waiting_for_msg)(send_msg_to_all)
    dp.callback_query(lambda c: c.data == "send_all")(send_all)
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
    dp.callback_query(lambda c: c.data == "anime_category")(anime_category)
    dp.callback_query(lambda c: c.data == "manga_category")(manga_category)
    dp.callback_query(lambda c: c.data in [*category_list,"category_done"])(categorys)
    dp.callback_query(lambda c: c.data in ["admin_btn_o1","admin_btn_o2"])(add_other_name) 
    dp.callback_query(lambda c: c.data.startswith("anime_"))(searched_anime)
    dp.callback_query(lambda c: c.data.startswith("animepage_"))(searched_anime2)
    dp.callback_query(lambda c: c.data.startswith("manga_"))(searched_manga)
    dp.callback_query(lambda c: c.data.startswith("mangapage_"))(searched_manga2)
    dp.callback_query(lambda c: c.data.startswith("animeid_"))(anime_video)
    dp.callback_query(lambda c: c.data.startswith("mangaid_"))(manga_file)



