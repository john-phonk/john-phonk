from pyrogram import Client, filters
from pyrogram.types import Message
from ..utils.utils import modules_help, prefix


@Client.on_message(filters.command('test', prefix) & filters.me)
async def test(client: Client, message: Message):
    await message.edit('<code>This is an test module</code>')


modules_help.update({'test': '''test - test edit''',
                     'test module': 'Test: test'})
