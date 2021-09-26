from pyrogram import Client, filters
from pyrogram.types import Message
from ..utils.utils import modules_help, prefix

import asyncio


@Client.on_message(filters.command('voice_spam', prefix) & filters.me)
async def voice_spam(client: Client, message: Message):
    voice = message.reply_to_message.message_id
    quantity = message.command[1]
    chat_to = message.command[2]
    reply_to_message = int(message.command[3])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        msg = await client.copy_message(
            from_chat_id=message.chat.id,
            chat_id=chat_to,
            message_id=voice,
            reply_to_message_id=reply_to_message,
        )
        await asyncio.sleep(0.1)


modules_help.update(
    {
        'voice_spam': '''voice_spam [amount of spam] [chat_to (chat id)] [reply_to_message (msg id)] (reply to voice)- voice_spam''',
        'voice_spam module': 'voice_spam: voice_spam',
    }
)
