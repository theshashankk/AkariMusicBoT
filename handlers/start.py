from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJchtgfvsZvz3OOIlXFLoLmSayvZsRrAACdgEAAi296UdEmIVdxe3iSR8E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your group's voice chat😁🔥
**A perfect Music Player...**
\nTo add in your group contact us at @akari_support.
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚪ SUPPORT GROUP ⚪", url="https://t.me/akari_support",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⚪ CHANNEL ⚪", url="https://t.me/AkariSupport"
                    ),
                    InlineKeyboardButton(
                        "⚪ CREATOR ⚪", url="https://t.me/ThesedLyf"
                    ),
                    InlineKeyboardButton(
                        "🎛️ COMMAND 🎛️", url="https://telegra.ph/Akari-Music-Bot-04-20"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Akari_MusicBoT?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
