# -*- coding: utf-8 -*-
"""
Jadidlar Izidan Telegram Boti (@Jadidlar_bilan_tanishtiruvchibot)
Muallif: Elshodbek Lutfullayev
Render.com ga moslashtirilgan (Health Check Port + Aiogram Polling)
"""

import os
import sys
import asyncio
import logging
import random
from aiohttp import web
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
    InputMediaPhoto
)

from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Jadidlar ma'lumotlari
from jadidlar_data import JADIDLAR, QUIZ_QUESTIONS

# Log sozlamalari
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Tokenni olish (.env yoki Render Environment Variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

if not BOT_TOKEN:
    # Standart zaxira (agar test qilinayotgan bo'lsa)
    logger.warning("DIQQAT: BOT_TOKEN o'zgaruvchisi topilmadi. Render Environment Variables yoki .env ga qo'ying.")

bot = Bot(token=BOT_TOKEN) if BOT_TOKEN else None
dp = Dispatcher()

# --- Klaviaturalar ---

def get_main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📚 Jadidlar ro'yxati"), KeyboardButton(text="🔍 Jadidni qidirish")],
            [KeyboardButton(text="📜 Hikmatli so'zlar"), KeyboardButton(text="🧠 Viktorina (Test)")],
            [KeyboardButton(text="ℹ️ Bot haqida")]
        ],
        resize_keyboard=True
    )

def get_jadidlar_inline_keyboard():
    buttons = []
    # 2 tadan qilib joylaymiz
    row = []
    for key, data in JADIDLAR.items():
        row.append(InlineKeyboardButton(text=data["name"], callback_data=f"jadid:{key}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_detail_keyboard(current_key):
    keys = list(JADIDLAR.keys())
    keys.remove(current_key)
    random_key = random.choice(keys)
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🎲 Tasodifiy jadid", callback_data=f"jadid:{random_key}"),
                InlineKeyboardButton(text="📚 Barcha jadidlar", callback_data="list_all")
            ]
        ]
    )

# --- Matn tayyorlash ---

def format_jadid_caption(data):
    caption = (
        f"🌟 <b>{data['name']}</b>\n"
        f"<i>{data['title']}</i>\n\n"
        f"📅 <b>Tug'ilgan sanasi:</b> {data['birth_date']}\n"
        f"📍 <b>Tug'ilgan joyi:</b> {data['birth_place']}\n"
        f"🕊 <b>Vafoti / Qatag'on:</b> {data['death_date']}\n\n"
        f"📖 <b>Hayoti va faoliyati:</b>\n{data['bio']}\n\n"
        f"✍️ <b>Mashhur asarlari:</b>\n" + "\n".join([f"• {w}" for w in data['works']]) + "\n\n"
        f"💬 <b>Hikmatli so'zi:</b>\n<i>{data['quote']}</i>"
    )
    return caption

# --- Handlerlar ---

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    welcome_text = (
        "Assalomu alaykum va rahmatullohi va barakatuh!\n\n"
        "🏛 <b>«Jadidlar izidan»</b> ma'rifiy botiga xush kelibsiz!\n\n"
        "Ushbu bot XX asr boshida millatimizning erki, ilm-ma'rifati va taraqqiyoti yo'lida "
        "jon fido qilgan <b>Jadid ma'rifatparvar allomalari</b> hayoti va ijodini o'rganish uchun yaratilgan.\n\n"
        "✨ <i>Quyidagi tugmalardan birini tanlang yoki alloma nomini yozib yuboring:</i>"
    )
    await message.answer(welcome_text, parse_mode="HTML", reply_markup=get_main_keyboard())

@dp.message(F.text == "📚 Jadidlar ro'yxati")
async def show_jadidlar_list(message: types.Message):
    await message.answer(
        "Quyidagi jadid allomalaridan birini tanlang va uning hayoti, surati hamda ijodi bilan tanishing:",
        reply_markup=get_jadidlar_inline_keyboard()
    )

@dp.callback_query(F.data.startswith("jadid:"))
async def callback_jadid(callback: CallbackQuery):
    jadid_key = callback.data.split(":")[1]
    if jadid_key in JADIDLAR:
        data = JADIDLAR[jadid_key]
        caption = format_jadid_caption(data)
        reply_markup = get_detail_keyboard(jadid_key)
        
        # Surat bilan yuborish
        try:
            await callback.message.delete()
        except Exception:
            pass
            
        try:
            await callback.message.answer_photo(
                photo=data["photo_url"],
                caption=caption,
                parse_mode="HTML",
                reply_markup=reply_markup
            )
        except Exception as e:
            logger.error(f"Rasm yuklashda xatolik: {e}")
            await callback.message.answer(
                caption,
                parse_mode="HTML",
                reply_markup=reply_markup
            )
    await callback.answer()

@dp.callback_query(F.data == "list_all")
async def callback_list_all(callback: CallbackQuery):
    await callback.message.answer(
        "Barcha jadid allomalari ro'yxati:",
        reply_markup=get_jadidlar_inline_keyboard()
    )
    await callback.answer()

@dp.message(F.text == "📜 Hikmatli so'zlar")
async def send_random_quote(message: types.Message):
    jadid_key = random.choice(list(JADIDLAR.keys()))
    data = JADIDLAR[jadid_key]
    text = (
        f"📜 <b>{data['name']} hikmati:</b>\n\n"
        f"<i>{data['quote']}</i>\n\n"
        f"— {data['name']}"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Batafsil ma'lumot", callback_data=f"jadid:{jadid_key}")],
            [InlineKeyboardButton(text="🔄 Yana bir hikmat", callback_data="next_quote")]
        ]
    )
    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)

@dp.callback_query(F.data == "next_quote")
async def callback_next_quote(callback: CallbackQuery):
    jadid_key = random.choice(list(JADIDLAR.keys()))
    data = JADIDLAR[jadid_key]
    text = (
        f"📜 <b>{data['name']} hikmati:</b>\n\n"
        f"<i>{data['quote']}</i>\n\n"
        f"— {data['name']}"
    )
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Batafsil ma'lumot", callback_data=f"jadid:{jadid_key}")],
            [InlineKeyboardButton(text="🔄 Yana bir hikmat", callback_data="next_quote")]
        ]
    )
    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
    await callback.answer()

@dp.message(F.text == "🧠 Viktorina (Test)")
async def send_quiz(message: types.Message):
    quiz = random.choice(QUIZ_QUESTIONS)
    await message.answer_poll(
        question=quiz["question"],
        options=quiz["options"],
        type="quiz",
        correct_option_id=quiz["correct"],
        explanation=quiz["explanation"],
        is_anonymous=False
    )

@dp.message(F.text == "🔍 Jadidni qidirish")
async def prompt_search(message: types.Message):
    await message.answer(
        "Istalgan jadid nomini yozing (masalan: <i>Behbudiy</i>, <i>Qodiriy</i>, <i>Cho'lpon</i>, <i>Avloniy</i>, <i>Fitrat</i>):",
        parse_mode="HTML"
    )

@dp.message(F.text == "ℹ️ Bot haqida")
async def about_bot(message: types.Message):
    text = (
        "🤖 <b>«Jadidlar izidan» boti haqida</b>\n\n"
        "Bu bot yosh avlodga Turkiston jadid allomalari, ularning millat ma'rifati va mustaqilligi yo'lidagi "
        "fidokorona xizmatlari haqida chuqur, haqqoniy va qiziqarli ma'lumot berish maqsadida yaratilgan.\n\n"
        "✨ <b>Asosiy xususiyatlari:</b>\n"
        "• Allomalarning qachon va qayerda tug'ilgani\n"
        "• Tarixiy fotosuratlari\n"
        "• Ilmiy va adabiy merosi, asarlari\n"
        "• Hikmatli so'zlari va ibratli faoliyati\n"
        "• Bilimlarni sinash uchun viktorina testlar\n\n"
        "👤 <b>Yaratuvchi:</b> Elshodbek Lutfullayev\n"
        "🚀 <b>Hosting:</b> Render.com"
    )
    await message.answer(text, parse_mode="HTML")

# Erkin qidiruv (foydalanuvchi ixtiyoriy matn yozganda)
@dp.message(F.text)
async def search_jadid(message: types.Message):
    query = message.text.lower().strip()
    
    # Jadidlar orasidan qidiramiz
    matches = []
    for key, data in JADIDLAR.items():
        if (query in data["name"].lower() or 
            query in data["title"].lower() or 
            query in data["birth_place"].lower() or
            any(query in work.lower() for work in data["works"])):
            matches.append((key, data))
            
    if len(matches) == 1:
        key, data = matches[0]
        caption = format_jadid_caption(data)
        try:
            await message.answer_photo(
                photo=data["photo_url"],
                caption=caption,
                parse_mode="HTML",
                reply_markup=get_detail_keyboard(key)
            )
        except Exception:
            await message.answer(caption, parse_mode="HTML", reply_markup=get_detail_keyboard(key))
    elif len(matches) > 1:
        buttons = [[InlineKeyboardButton(text=d["name"], callback_data=f"jadid:{k}")] for k, d in matches]
        await message.answer(
            f"🔎 «{message.text}» bo'yicha bir nechta alloma topildi:",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons)
        )
    else:
        await message.answer(
            "Kechirasiz, ushbu so'rov bo'yicha ma'lumot topilmadi.\n"
            "Alloma nomini to'g'ri yozganingizga ishonch hosil qiling yoki quyidagi tugmadan foydalaning:",
            reply_markup=get_main_keyboard()
        )

# --- Render.com Webhook / Health Server ---
async def handle_ping(request):
    return web.Response(text="Bot is running smoothly on Render!")

async def start_web_server():
    port = int(os.environ.get("PORT", 8080))
    app = web.Application()
    app.router.add_get("/", handle_ping)
    app.router.add_get("/health", handle_ping)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logger.info(f"Render uchun veb-server {port} portida ishga tushdi.")

async def main():
    if not bot:
        logger.error("BOT_TOKEN ko'rsatilmagan! Iltimos, BOT_TOKEN ni o'rnating.")
        return

    # Render uchun yengil veb-serverni ishga tushiramiz (Render o'chirib tashlamasligi uchun)
    asyncio.create_task(start_web_server())

    logger.info("Bot Render.com da ishga tushmoqda...")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
