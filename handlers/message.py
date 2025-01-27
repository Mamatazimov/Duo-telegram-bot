from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from utils import anime,manga
from keyboards.inline import search_kb,random_kb

class Main_menu(StatesGroup):
    waiting_for_anime_name = State()


# Start messages
async def main_menu(message: Message,state: FSMContext):
    if message.text == "Izlash 🔍":
        await message.answer("Izlayotgan animeyingiz yoki manga nomini kiriting 📝")
        await state.set_state(Main_menu.waiting_for_anime_name)

    elif message.text == "Kategoriyalar 📚":
        await message.answer("Quyidagi kategoriyalarni tanlashingiz mumkin 👇")

    elif message.text == "Tasodifiy 🎲":
        await message.answer("Tasodifiy anime kerakmi yoki manga 🎲",reply_markup=random_kb())


async def search_anime(message: Message,state: FSMContext):
    name = message.text
    anime_list = anime.searching_anime(name)
    if not anime_list:
        await message.answer("Bunday nomli anime yoki manga topilmadi :(")
    else:
        await message.answer("Quyidagi anime va mangalar topildi :) 👇",reply_markup=search_kb(name))





# Admin
# 1Admin: Anime 
# 1Anime: Yangi animeni bazada yaratish uchun so'rov
async def new_anime_series_msg(message: Message,state: FSMContext):
    name = message.text
    print(2)
    anime_names = anime.get_all_anime_names()
    if name in anime_names.keys():
        print(1)
        
        await message.answer(f"Bu nomda anime mavjud:\n {name} : {anime_names[name]}")
    else:
        print(0)
        anime.add_anime_name(anime_name=name)
        anime_id = anime.get_anime_id(anime_name=name)
        await message.answer(f"Nomi: {name}\nAnime id: {anime_id[0]}")
        await state.clear()


#2Anime: Anime qismlarini bazaga yuklash uchun so'rov
async def add_series_msg(message: Message,state: FSMContext):
    try:
        video_id = message.video.file_id
        if len(message.caption.split(" ",2)) == 2:
            anime_id,series_id = message.caption.split(" ",2)
            anime.add_anime_video(video_id=video_id,series_id=series_id,anime_id=anime_id)
            await message.answer(f"Video id: {video_id} va id: {anime_id} va qism: {series_id}")
            await state.clear()
        else:
            await message.answer("Video fayli yuklanmadi")
    except Exception as e:
        await message.answer(f"Xatolik : {e}")
        await state.clear()


#3Anime: Anime qismlarini o'chirish uchun so'rov
async def delete_series_msg(message: Message,state: FSMContext):
    try:
        anime_ids = list(anime.get_all_anime_names().values())
        if len(message.text.split(" ",2)) == 2:
            alen = 2
        elif len(message.text.split(" ",2)) == 1:
            alen = 1

        if alen == 2:
            if int(message.text.split(" ")[0]) in anime_ids:
                if len(message.text.split(" ",2)) == 2:
                    anime_id,series_id = map(int,message.text.split(" ",2))
                    anime.delete_anime_seria(anime_id,series_id)
                    await message.answer(f"Anime id: {anime_id}\nQism raqami: {series_id}")
                    await state.clear()
                else:
                    await message.answer("Fayl o'chmadi")
                    await state.clear()
            else:
                await message.answer("Bunday idlik anime topilmadi")
                await state.clear()

        elif alen == 1:
            if int(message.text) in anime_ids:
                anime_id = message.text
                anime.delete_anime(anime_id)
                await message.answer(f"Anime o'chirildi: {anime_id}")
                await state.clear()
            else:
                await message.answer("Bunday id topilmadi")
                await state.clear()
        else:
            await message.answer("Bunday idlik anime topilmadi")
            state.clear()
    except Exception as e:
        await message.answer(f"Xatolik : {e}")
        await state.clear()

# 2Admin: Manga
# 1Manga: Yangi animeni bazada yaratish uchun so'rov
async def new_manga_series_msg(message: Message,state: FSMContext):
    name = message.text
    manga.add_manga_name(anime_name=name)
    await message.answer(f"Nomi: {name}")
    await state.clear()


#2Manga: Manga qismlarini bazaga yuklash uchun so'rov
async def add_manga_series_msg(message: Message,state: FSMContext):
    id = message.document.file_id
    if len(message.caption.split(" ",2)) == 2:
        manga_id,series_id = message.caption.split(" ",2)
        manga.add_manga_file(id,series_id,manga_id)
        await message.answer(f"File id: {id} va id: {manga_id} va qism: {series_id}")
        await state.clear()
    else:
        await message.answer("Fayl yuklanmadi")
        await state.clear()


#3Manga: Manga qismlarini o'chirish uchun so'rov
async def delete_manga_series_msg(message: Message,state: FSMContext):
    try:
        manga_ids = list(manga.get_all_manga_names().values())
        if len(message.text.split(" ",2)) == 2:
            alen = 2
        elif len(message.text.split(" ",2)) == 1:
            alen = 1

        if alen == 2:
            if int(message.text.split(" ")[0]) in manga_ids:
                if len(message.text.split(" ",2)) == 2:
                    manga_id,series_id = map(int,message.text.split(" ",2))
                    manga.delete_manga_seria(manga_id,series_id)
                    await message.answer(f"Manga id: {manga_id}\nQism raqami: {series_id}")
                    await state.clear()
                else:
                    await message.answer("Fayl o'chmadi")
                    await state.clear()
            else:
                await message.answer("Bunday idlik manga topilmadi")
                await state.clear()

        elif alen == 1:
            if int(message.text) in manga_ids:
                manga_id = message.text
                manga.delete_manga(manga_id)
                await message.answer(f"Manga o'chirildi: {manga_id}")
                await state.clear()
            else:
                await message.answer("Bunday id topilmadi")
                await state.clear()
        else:
            await message.answer("Bunday idlik manga topilmadi")
            state.clear()
    except Exception as e:
        await message.answer(f"Xatolik : {e}")
        await state.clear()


async def add_category_msg(message: Message,state: FSMContext):
    print("ish")
    msg_list = message.text.split(",")
    c,id = msg_list.pop(0).split("_")
    id = int(id)
    msg=""
    print("ish1")
    for i in msg_list:
        msg+=i+","
    print("ish2")
    if c == "anime":
        print(1)
        anime.add_category(id,msg)
        await message.answer(f"Anime: {anime.get_anime_name(id)[0]}\nKategoriya: {msg}")
        state.clear()
    elif c == "manga":
        print(2)
        manga.add_category(id,msg)
        await message.answer(f"Manga: {manga.get_manga_name(id)[0]}\nKategoriya: {msg}")
        state.clear()

async def rem_category_msg(message: Message,state: FSMContext):
    c,id = message.text.split("_")
    id = int(id)
    if c == "anime":
        print(11)
        anime.rem_category(id)
        await message.answer(f"Anime: {anime.get_anime_name(id)[0]}\nKategoriya bo'shatildi")
        state.clear()
    elif c == "manga":
        print(22)
        manga.rem_category(id)
        await message.answer(f"Manga: {manga.get_manga_name(id)[0]}\nKategoriya bo'shatildi")
        state.clear()









