import random
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils import anime,manga
from keyboards.inline import series_kb,chapter_kb,admin_category_kb



class Anime(StatesGroup):
    waiting_for_name = State()
    waiting_for_video = State()
    waiting_for_anime_id = State()

class Manga(StatesGroup):
    waiting_for_name = State()
    waiting_for_file = State()
    waiting_for_file_id = State()

class Anime_film(StatesGroup):
    waiting_for_name = State()
    waiting_for_video = State()
    waiting_for_anime_id = State()

class Category(StatesGroup):
    waiting_for_amsg = State()
    waiting_for_rmsg = State()


# Admin
# 1Admin: Anime 
# 1Anime: Yangi animeni bazada yaratish uchun so'rov
async def new_anime_series(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Yangi anime seriasi qo'shish uchun uning nomini jo'nating")
    await state.set_state(Anime.waiting_for_name)

#2Anime: Anime qismlarini bazaga yuklash uchun so'rov
async def add_series(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Anime qismlarini bazaga yuklash uchun video faylini yuboring va contextning birinchi raqamiga anime idsini va probel(' ') tashab uni qismini yozing:\n (2 6) 2 bu uning idsi va 6 uning qismi.")
    await state.set_state(Anime.waiting_for_video)

#3Anime: Anime qismlarini o'chirish uchun so'rov
async def delete_series(call: CallbackQuery,state: FSMContext):
    await call.message.answer("O'chirish uchun anime id ni yuboring. Agar context 1ta raqamdan iborat bo'lsa uni shu id dagi animeni butunlay o'chirib tashlaydi.\nAgar biror bir qismni o'chirmoqchi bo'lsangiz anime idsini birinchi va uni qismini ikkinchi yuboring , o'rtasini probel bilan ajrating.\nNamuna: (3 4) 3-idli animeni 4-qismi o'chadi.\nNamuna: (4) 4-idli anime butunlay o'chib ketti")
    await state.set_state(Anime.waiting_for_anime_id)

# 2Admin: Manga
# 1Manga: Yangi mangani bazada yaratish uchun so'rov
async def new_manga_series(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Yangi manga seriasi qo'shish uchun uning nomini jo'nating")
    await state.set_state(Manga.waiting_for_name)

#2Manga: manga qismlarini bazaga yuklash uchun so'rov
async def add_manga_series(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Manga qismlarini bazaga yuklash uchun faylini yuboring va contextning birinchi raqamiga anime idsini va probel(' ') tashab uni qismini yozing:\n (2 6) 2 bu uning idsi va 6 uning qismi.")
    await state.set_state(Manga.waiting_for_file)

#3Manga: manga qismlarini o'chirish uchun so'rov
async def delete_manga_series(call: CallbackQuery,state: FSMContext):
    await call.message.answer("O'chirish uchun manga id ni yuboring. Agar context 1ta raqamdan iborat bo'lsa uni shu id dagi animeni butunlay o'chirib tashlaydi.\nAgar biror bir qismni o'chirmoqchi bo'lsangiz anime idsini birinchi va uni qismini ikkinchi yuboring , o'rtasini probel bilan ajrating.\nNamuna: (3 4) 3-idli animeni 4-qismi o'chadi.\nNamuna: (4) 4-idli anime butunlay o'chib ketti")
    await state.set_state(Manga.waiting_for_file_id)

async def all_anime_series_msg(cq: CallbackQuery ):
    anime_list = anime.get_all_anime_names()
    if anime_list == {}:
        await cq.message.answer("Anime list bo'sh")
    else:
        msg = "Barcha animelar va ularni idsi"
        for i,id in anime_list.items():
            msg += f"\n{i} : {id} "
        await cq.message.answer(f"Anime list: {msg}")

async def all_manga_series_msg(cq: CallbackQuery):
    manga_list = manga.get_all_manga_names()
    if manga_list == {}:
        await cq.message.answer("Manga list bo'sh")
    else:
        msg = "Barcha mangalar va ularni idsi"
        for i, id in manga_list.items():
            msg += f"\n{i} : {id} "
        await cq.message.answer(f"Manga list: {msg}")

async def searched_anime(call: CallbackQuery,id=None):
    id = call.data.split("_")[1] if id is None else id
    anime_series = anime.get_anime_series(id)
    anime_name = anime.get_anime_name(id)
    
    if not anime_series:
        await call.message.answer("Bu anime uchun qismlar topilmadi :(")
    else:
        await call.message.answer(f"Anime: {anime_name[0]}\nQismlar:", reply_markup=series_kb(id))
 
async def searched_manga(call: CallbackQuery,id=None):
    id = call.data.split("_")[1] if id is None else id
    manga_series = manga.get_manga_series(id)
    manga_name = manga.get_manga_name(id)
    
    if not manga_series:
        await call.message.answer("Bu manga uchun qismlar topilmadi :(")
    else:
        await call.message.answer(f"Manga: {manga_name[0]}\nQismlar:", reply_markup=chapter_kb(id))

async def anime_video(call: CallbackQuery,anime_id=None,series_id=None):
    from main import bot
    anime_id = call.data.split("_")[1] if anime_id is None else anime_id
    seria_id = call.data.split("_")[2] if series_id is None else series_id

    anime_video_id = anime.get_anime_seria(anime_id,seria_id)[0]
    chat_id = call.message.chat.id
    await bot.send_video(chat_id=chat_id, video=anime_video_id, caption=f"Anime: {anime.get_anime_name(anime_id)[0]}\nQism: {seria_id}")

async def manga_file(call: CallbackQuery,manga_id=None,series_id=None):
    from main import bot
    manga_id = call.data.split("_")[1] if manga_id is None else manga_id
    seria_id = call.data.split("_")[2] if series_id is None else series_id

    manga_file_id = manga.get_manga_seria(manga_id,seria_id)[0]
    chat_id = call.message.chat.id
    await bot.send_document(chat_id=chat_id, document=manga_file_id, caption=f"Manga: {manga.get_manga_name(manga_id)[0]}\nQism: {seria_id}")

async def random_anime(call: CallbackQuery):
    anime_list = anime.get_all_anime_names()
    anime_id = random.choice(list(anime_list.values()))
    anime_series = anime.get_anime_series(anime_id)
    anime_name = anime.get_anime_name(anime_id)
    if not anime_series:
        await call.message.answer("Bu anime uchun qismlar topilmadi :(")
    else:
        await call.message.answer(f"Anime: {anime_name[0]}\nQismlar:", reply_markup=series_kb(anime_id))

async def random_manga(call: CallbackQuery):
    manga_list = manga.get_all_manga_names()
    manga_id = random.choice(list(manga_list.values()))
    manga_series = manga.get_manga_series(manga_id)
    manga_name = manga.get_manga_name(manga_id)
    if not manga_series:
        await call.message.answer("Bu manga uchun qismlar topilmadi :(")
    else:
        await call.message.answer(f"Manga: {manga_name[0]}\nQismlar:", reply_markup=chapter_kb(manga_id))

async def category(call: CallbackQuery):
    await call.message.answer("Quyidaqilardan birini tanlang👇",reply_markup=admin_category_kb())

async def add_category(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Namuna:manga_1,romantika,shoujo,isekai")
    await state.set_state(Category.waiting_for_amsg)

async def rem_category(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Namuna:manga_1,romantika,shoujo,isekai")
    await state.set_state(Category.waiting_for_rmsg)






