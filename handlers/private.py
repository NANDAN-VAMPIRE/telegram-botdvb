import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://https://telegra.ph/file/773dd8099b972a868065a.jpg",
        caption=f"""**ᴛʜɪꜱ ᴍᴜꜱɪᴄ ʙᴏᴛ ɪꜱ ᴀᴅᴠᴀɴᴄᴇ ᴀɴᴅ ɴᴏ ʟᴀɢ ᴜꜱᴇ ɪᴛ ᴄᴏɴᴛɪɴᴜᴏᴜꜱʟʏ .
                 ᴄᴏᴅᴇʀ :- [ʙᴀᴅᴇ ʟᴏɢ](https://t.me/bhumihar_op1)
      ɪꜰ ʏᴏᴜ ᴀɴʏ ᴘʀᴏʙʟᴇᴍ ᴛᴇʟʟ ʜᴇʀᴇ = [ʙᴀᴅᴇ ʟᴏɢ](https://t.me/bhumihar_op1)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💕 ᴄʟᴜꜱᴛᴇʀ 💫", url=f"https://t.me/+oDnTqMzvs7w1MWVl")
                ]
                
           ]
        ),
    )

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://https://telegra.ph/file/773dd8099b972a868065a.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.

┏━━━━━━━━━━━━━━━━━┓
┣★ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃   » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/bhumihar_op1)
┣★ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/parul_x_support)
┣★ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 ➪ » [𝐂𝐥𝐢𝐜𝐤 𝐇𝐞𝐫𝐞](https://t.me/brandinvisible_brothers)
┗━━━━━━━━━━━━━━━━━┛

💞 𝐉𝐮𝐬𝐭 𝐀𝐝𝐝 𝐌𝐞 » 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 𝐀𝐧𝐝
𝐄𝐧𝐣𝐨𝐲 𝐒𝐮𝐩𝐞𝐫 𝐐𝐮𝐚𝐥𝐢𝐭𝐲 ❥︎𝐌𝐮𝐬𝐢𝐜.
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ 𝐀𝐝𝐝 𝐌𝐞 𝐓𝐨 𝐘𝐨𝐮𝐫 𝐆𝐫𝐨𝐮𝐩 ❱ ➕", url=f"https://t.me/ALONEX_MUSIC_BOT?startgroup=true")
                ]
                
           ]
        ),
    )
    

