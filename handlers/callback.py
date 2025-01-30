import random
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils import anime,manga,referral
from keyboards.inline import series_kb,chapter_kb,admin_category_kb,anime_category_kb,search_category_kb
from config import category_list



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

class Send_msg(StatesGroup):
    waiting_for_msg = State()

class Other_name(StatesGroup):
    waiting_for_names = State()

data = {}
list_for_data = []
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

async def searched_anime(call: CallbackQuery):
    id = call.data.split("_")[1]
    anime_series = anime.get_anime_series(id)
    anime_name = anime.get_anime_name(id)
    if not anime_series:
        await call.message.answer("Bu anime uchun qismlar topilmadi :(")
    else:
        await call.message.answer(f"Anime: {anime_name[0]}\nQismlar:", reply_markup=series_kb(id,current_page=1))

async def searched_anime2(call: CallbackQuery):
    id = int(call.data.split("_")[2])
    
    current_page = call.data.split("_")[1]
    anime_series = anime.get_anime_series(id)
    anime_name = anime.get_anime_name(id)
    if not anime_series:
        await call.message.answer(f"Bu anime uchun qismlar topilmadi :({id}")
    else:
        try:
            await call.message.edit_text(f"Anime: {anime_name[0]}\nQismlar:", reply_markup=series_kb(id,current_page=current_page))
        except ValueError:
            await call.answer("Bu sahifa yo'q❗")
 
async def searched_manga(call: CallbackQuery):
    id = call.data.split("_")[1]
    manga_series = manga.get_manga_series(id)
    manga_name = manga.get_manga_name(id)
    
    if not manga_series:
        await call.message.answer("Bu manga uchun qismlar topilmadi :(")
    else:
        await call.message.answer(f"Manga: {manga_name[0]}\nQismlar:", reply_markup=chapter_kb(id,current_page=1))

async def searched_manga2(call: CallbackQuery):
    id = int(call.data.split("_")[2])

    current_page = call.data.split("_")[1]
    manga_series = manga.get_manga_series(id)
    manga_name = manga.get_manga_name(id)
    if not manga_series:
        await call.message.answer(f"Bu manga uchun qismlar topilmadi :({id}")
    else:
        try:
            await call.message.edit_text(f"Manga: {manga_name[0]}\nQismlar:", reply_markup=chapter_kb(id, current_page=current_page))
        except ValueError:
            await call.answer("Bu sahifa yo'q❗")

async def anime_video(call: CallbackQuery):
    from main import bot
    anime_id = call.data.split("_")[1]
    seria_id = call.data.split("_")[2]

    anime_video_id = anime.get_anime_seria(anime_id,seria_id)[0]
    chat_id = call.message.chat.id
    await bot.send_video(chat_id=chat_id, video=anime_video_id, caption=f"Anime: {anime.get_anime_name(anime_id)[0]}\nQism: {seria_id}")

async def manga_file(call: CallbackQuery):
    from main import bot
    manga_id = call.data.split("_")[1]
    seria_id = call.data.split("_")[2]

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

async def anime_category(call: CallbackQuery):
    data[call.message.chat.id] = {"value":""}
    list_for_data.append("anime")
    await call.message.answer("Anime categoriyalari:",reply_markup=anime_category_kb())

async def manga_category(call: CallbackQuery):
    data[call.message.chat.id] = {"value":""}
    list_for_data.append("manga")
    await call.message.answer("Manga categoriyalari:",reply_markup=anime_category_kb())

async def categorys(call: CallbackQuery):
    from main import bot
    chat_id = call.message.chat.id
    message_id = call.message.message_id
 
    for category in category_list:
        if call.data == category:
            data[chat_id]["value"] += f"{category} ,"
    if call.data == "category_done":
        try:
            final_value = data[chat_id]["value"]
            final_value = final_value[:-1]
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Siz tanlagan categoriyalar: <i>{final_value}</i>",reply_markup=None)
            await finish_category_data(chat_id,final_value,message_id)
            return
        except TypeError as e:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Type error:{e}",reply_markup=None)
            return
        except Exception as e:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Xatolik yuz berdi, /help:{e}",reply_markup=None)
            return

    current_value = data[chat_id]["value"]
    await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=f"Tanlangan categoriyalar: <i>{current_value}</i>",reply_markup=call.message.reply_markup)

async def finish_category_data(chat_id,final_value,message_id):
    from main import bot
    qiymat = list_for_data.pop()
    value_list=final_value.split(",")
    values_list = list(set(value_list))
    for i in values_list:
        values_list.remove(i)
        i = i.strip()
        values_list.append(i)
    if "" in values_list:
        await bot.edit_message_text(chat_id=chat_id,message_id=message_id,text="Iltimos categoriyalarda birini tanlang❗")
        return
    if qiymat == "anime":
        animes_id_list = anime.anime_category_search(values_list)
        await bot.edit_message_text(chat_id=chat_id,text="Natija👇:",message_id=message_id,reply_markup=search_category_kb(animes_id_list,qiymat=qiymat))
    elif qiymat == "manga":
        manga_id_list = manga.manga_category_search(values_list)
        await bot.edit_message_text(chat_id=chat_id,text="Natija👇:",message_id=message_id,reply_markup=search_category_kb(manga_id_list,qiymat=qiymat))
    data[chat_id]["value"] = ""

async def add_other_name(call: CallbackQuery,state: FSMContext):
    data = call.data
    await call.message.answer("Qo'shmoqchi bo'lgan animelarni nomini quydagicha kiriting:\nNamuna: 34_anime1,anime2,anime3/nBundan 34 id va qolgan qism esa qo'shimcha nomlar")
    await state.set_state(Other_name.waiting_for_names)
    await state.update_data(data_key=data)

async def stats(call: CallbackQuery):
    users_num = len(referral.get_all_users())
    await call.message.answer(f"Barcha obunachi: {users_num}")

async def send_all(call: CallbackQuery,state: FSMContext):
    await call.message.answer("Jo'natiladigan xabarni yuboring!")
    await state.set_state(Send_msg.waiting_for_msg)





