from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp




@dp.message_handler(commands="image")
async def send_images(message: types.Message):
    url="http://127.0.0.1:8000/dogs/?format=json"
    response=request.get(url)
    data=response.json()

    for item in data:
        image_url=item['image']
        name=item['name']


        image_response=request.get(image_url)
        if image_response.status_code==200:
            image_bytes=BytesIQ(image_response.content)
            await message.reply_photo(photo=image_bytes,caption=name)
        else:
            await message.reply(f"Rasmni yuklab olishda xatolik yuz berdi: {image_url}")



