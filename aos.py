from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

bot = Client(
    "TEST", api_id=13429252, api_hash="33d94e2daae5c7777f0d9b59a72ab0a6",
    bot_token="5559289362:AAFVfL0o4t4LnjLmBwG_8blgBSxQZF6HsyM")


@bot.on_message(filters.command('start'))
def command1(_, message):
    bot.send_message(message.chat.id, "مرحبا بك في بوت TEST")


botton = [
    [InlineKeyboardButton('تواصل', url='https://t.me/AS222002'),
     InlineKeyboardButton('دليل الاستخدام', "لم يتم تجهيزه بعد")]
]


@bot.on_message(filters.command('help'))
def command1(_, message):
    text = "كيف يمكنني مساعدتك"
    reply_markup = InlineKeyboardMarkup(botton)
    message.reply(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )

@bot.on_message(filters.regex('مرحبا'))
def command2(_, message):
    message.reply_text("أهلا وسهلا")


@bot.on_message(filters.regex('صورة'))
def command3(_, message):
    bot.send_photo(message.chat.id, "https://imgur.com/gallery/wYTCtRu")


@bot.on_message(filters.new_chat_members)
def hi(_, message):
    message.reply_text("مرحبا بالعضو الجديد")


bot.run()

