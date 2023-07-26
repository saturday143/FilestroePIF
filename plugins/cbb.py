#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == buttons = [
            [
                InlineKeyboardButton('❣️ 𝐔𝐏𝐃𝐀𝐓𝐄𝐒 ❣️', url='https://t.me/BoTzUpdates0')
            ],
            [
                InlineKeyboardButton('⚡ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ⚡', url=f"https://t.me/PanindiaFilmz"),
            ],
            [
                InlineKeyboardButton(text=DOWNLOAD_TEXT_NAME,url=DOWNLOAD_TEXT_URL)
            ]
            [
                InlineKeyboardButton('⚡ 𝐏𝐚𝐧𝐈𝐧𝐝𝐢𝐚𝐅𝐥𝐢𝐦𝐙  ⚡', url=f"https://t.me/PanindiaFilmz"),
            ]
    ]
    
    "about":
        await query.message.edit_text(
            text = f"<b>○ Creator : <a href='tg://user?id={6693334935}'>@PIFOficial_Dev</a>\n○ Language : <code>Python3</code>\n○ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n○ Source Code : <a href='DevLOVEper'>click here</a>\n○ Channel : @PanindiaFilmz\n○ Support Group : @BoTzUpdates0</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
