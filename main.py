
import os, cv2
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from cartooner import cartoonize
from animegan import apply_anime_style

bot = Bot(token=os.getenv("AAFKlFxnALsn_2Mj3SE3vS1qJHvVU1KQMYg"))
dp = Dispatcher(bot)
users = {}

style_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("🎨 Cartoon"), KeyboardButton("🌸 Hayao"),
    KeyboardButton("🎬 Shinkai"), KeyboardButton("🎥 Paprika"),
    KeyboardButton("✨ Pixar")
)

@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    users[msg.from_user.id] = "cartoon"
    await msg.answer("Выбери стиль:", reply_markup=style_markup)

@dp.message_handler(lambda m: m.text in ["🎨 Cartoon", "🌸 Hayao", "🎬 Shinkai", "🎥 Paprika", "✨ Pixar"])
async def set_style(msg: types.Message):
    style_map = {
        "🎨 Cartoon": "cartoon",
        "🌸 Hayao": "hayao",
        "🎬 Shinkai": "shinkai",
        "🎥 Paprika": "paprika",
        "✨ Pixar": "pixar"
    }
    style = style_map.get(msg.text, "cartoon")
    users[msg.from_user.id] = style
    await msg.reply(f"✅ Стиль установлен: {msg.text}")

@dp.message_handler(content_types=['photo'])
async def photo(msg: types.Message):
    await msg.answer("🧠 Обработка изображения...")
    in_path = "in.jpg"
    out_path = "out.jpg"
    await msg.photo[-1].download(in_path)

    style = users.get(msg.from_user.id, "cartoon")
    if style == "cartoon":
        img = cv2.imread(in_path)
        result = cartoonize(img)
        cv2.imwrite(out_path, result)
    else:
        apply_anime_style(in_path, out_path, model_name=style)

    await msg.answer_photo(types.InputFile(out_path))
