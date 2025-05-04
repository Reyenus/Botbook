from aiogram import Router
from aiogram.types import Message

router = Router()

#Реакция на любые, не предусмотренные, сообщения боту
@router.message()
async def send_echo(message: Message):
    await message.answer(f'Это эхо! {message.text}')