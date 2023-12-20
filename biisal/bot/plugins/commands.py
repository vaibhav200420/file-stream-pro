# (c) @biisal @adarsh

from biisal.bot import StreamBot
from biisal.vars import Var
import logging
logger = logging.getLogger(__name__)
from biisal.bot.plugins.stream import MY_PASS
from biisal.utils.human_readable import humanbytes
from biisal.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from biisal.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup
from biisal.vars import bot_name , bisal_channel , bisal_grp


SRT_TXT = """<b>ᴊᴀɪ sʜʀᴇᴇ ᴋʀsɴᴀ {}!,
I ᴀᴍ Fɪʟᴇ ᴛᴏ Lɪɴᴋ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ ᴡɪᴛʜ Cʜᴀɴɴᴇʟ sᴜᴘᴘᴏʀᴛ.

Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ sᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ.!
ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/biisal_bot'>Bɪɪsᴀʟ</a></b>"""

@StreamBot.on_message(filters.command("start") & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/5eb253f28ed7ed68cb4e6.png",
                caption=""""<b>Hᴇʏ ᴛʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/biisal_bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://telegra.ph/file/d813fe75a3ac675ef34b7.jpg",
    caption= SRT_TXT.format(m.from_user.mention(style="md")),
    reply_markup=InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🤡", url=bisal_channel)],
            [
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ 😎", callback_data="about"),
                 InlineKeyboardButton("ʜᴇʟᴘ 😅", callback_data="help")
            ],
            [InlineKeyboardButton("ᴏᴜʀ ɢʀᴏᴜᴘ 🚩", url=bisal_grp)],

            [
                 InlineKeyboardButton("ᴅɪsᴄʟᴀɪᴍᴇʀ 🔻", url=f"https://www.google.com"),
                 InlineKeyboardButton("ᴅᴇᴠ 😊", callback_data="aboutDev")
            ]
        ]
    )
)
@StreamBot.on_message(filters.command("help") & filters.private )
async def help_cd(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.NEW_USER_LOG,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__𝓢𝓞𝓡𝓡𝓨, 𝓨𝓞𝓤 𝓐𝓡𝓔 𝓐𝓡𝓔 𝓑𝓐𝓝𝓝𝓔𝓓 𝓕𝓡𝓞𝓜 𝓤𝓢𝓘𝓝𝓖 𝓜𝓔. 𝓒ᴏɴᴛᴀᴄᴛ ᴛʜᴇ 𝓓ᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **𝙃𝙚 𝙬𝙞𝙡𝙡 𝙝𝙚𝙡𝙥 𝙮𝙤𝙪**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/5eb253f28ed7ed68cb4e6.png",
                caption=""""<b>Hᴇʏ ᴛʜᴇʀᴇ!\n\nPʟᴇᴀsᴇ ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ ! 😊\n\nDᴜᴇ ᴛᴏ sᴇʀᴠᴇʀ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ !</b>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🚩", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<b>sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ.ᴘʟᴇᴀsᴇ <a href='https://t.me/biisal_bot'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ғᴏʀ sᴜᴘᴘᴏʀᴛ</a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
    chat_id=m.chat.id,
    photo="https://telegra.ph/file/d813fe75a3ac675ef34b7.jpg",
    caption=f"<b>ᴡᴇ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴍᴀɴʏ <a href='https://t.me/bisal_files'>ᴄᴏᴍᴍᴀɴᴅs</a> ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🤩.\n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ <a href='https://t.me/bisal_files'>ᴠɪᴅᴇᴏ ғɪʟᴇs</a> ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ <a href='https://t.me/bisal_files'>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍᴀʙʟᴇ</a> ʟɪɴᴋ.\n\nᴏʀ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ <a href='https://t.me/bisal_files'>ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a>..ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ 😎</b>",
    reply_markup=InlineKeyboardMarkup(
        [
            [   
                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🤡", url=bisal_channel)
            ],
            [
                InlineKeyboardButton("ᴅɪsᴄʟᴀɪᴍᴇʀ 🔻", url=f"https://www.google.com"),
                InlineKeyboardButton("ᴏᴜʀ ɢʀᴏᴜᴘ 🚩", url=bisal_grp),

            ],
            [
                InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),

            ]

        ]
    )
)



@StreamBot.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "close_data":
        await query.message.delete()


    if data == "start":
        await query.message.edit_caption(
        caption= SRT_TXT.format(query.from_user.mention(style="md")),
        reply_markup=InlineKeyboardMarkup(
                [
            [InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🤡", url=bisal_channel)],
            [
                 InlineKeyboardButton("ᴀʙᴏᴜᴛ 😎", callback_data="about"),
                 InlineKeyboardButton("ʜᴇʟᴘ 😅", callback_data="help")
            ],
            [InlineKeyboardButton("ᴏᴜʀ ɢʀᴏᴜᴘ 🚩", url=bisal_grp)],

            [
                 InlineKeyboardButton("ᴅɪsᴄʟᴀɪᴍᴇʀ 🔻", url=f"https://telegra.ph/Disclaimer-11-07-37"),
                 InlineKeyboardButton("ᴅᴇᴠ 😊", callback_data="aboutDev")
            ]
        ]
            )
        )

    
    elif data == "about":
        await query.message.edit_caption(
            caption=f"<b>Mʏ ɴᴀᴍᴇ :<a href='https://t.me/bisal_file2link_bot'>{bot_name}</a>\nAᴅᴍɪɴ : <a href='https://t.me/biisal_bot'>Bɪɪsᴀʟ</a>\nʜᴏsᴛᴇᴅ ᴏɴ : ʜᴇʀᴏᴋᴜ\nᴅᴀᴛᴀʙᴀsᴇ : ᴍᴏɴɢᴏ ᴅʙ\nʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3</b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                  ]]
            )
        )
    elif data == "help":
        await query.message.edit_caption(
        caption=f"<b>ᴡᴇ ᴅᴏɴᴛ ɴᴇᴇᴅ ᴍᴀɴʏ <a href='https://t.me/bisal_files'>ᴄᴏᴍᴍᴀɴᴅs</a> ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ 🤩.\n\nᴊᴜsᴛ sᴇɴᴅ ᴍᴇ <a href='https://t.me/bisal_files'>ᴠɪᴅᴇᴏ ғɪʟᴇs</a> ᴀɴᴅ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ <a href='https://t.me/bisal_files'>ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ & sᴛʀᴇᴀᴍᴀʙʟᴇ</a> ʟɪɴᴋ.\n\nᴏʀ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ɪɴ <a href='https://t.me/bisal_files'>ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ</a>..ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀɴᴅ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ ᴀɴᴅ sᴇᴇ ᴍʏ ᴍᴀɢɪᴄ 😎</b>",
            reply_markup=InlineKeyboardMarkup(
[[ 
                     InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                  ]]            )
        )
    elif data == "aboutDev":
        # please don't steal credit
        await query.message.edit_caption(
            caption=f"<b>ᴊᴀɪ sʜʀᴇᴇ ᴋʀsɴᴀ ᴅᴇᴀʀ...\nɪᴍ <a href='https://t.me/biisal_bot'>Bɪɪsᴀʟ</a>\nɪ ᴀᴍ ᴛʜᴇ ᴀᴅᴍɪɴ ᴏғ ᴛʜɪs ʙᴏᴛ..ᴀɴᴅ ɪ ᴍᴀᴅᴇ ᴛʜᴇ  ʙᴏᴛ ʙʏ ʜᴇʟᴘ ᴏғ <a href='https://github.com/adarsh-goel'>ᴀᴅᴀʀsʜ</a> ʙʀᴏ..\n\nGɪᴛʜᴜʙ : <a href='https://github.com/biisal'>Bɪɪsᴀʟ's Gɪᴛʜᴜʙ</a></b>",
            reply_markup=InlineKeyboardMarkup(
                [[ 
                     InlineKeyboardButton("ʜᴏᴍᴇ", callback_data="start"),
                     InlineKeyboardButton("ᴄʟᴏsᴇ ‼️", callback_data="close_data")
                  ]]            )
        )
