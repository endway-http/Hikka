# ---------------------------------------------------------------------------------
#░█▀▄░▄▀▀▄░█▀▄░█▀▀▄░█▀▀▄░█▀▀▀░▄▀▀▄░░░█▀▄▀█
#░█░░░█░░█░█░█░█▄▄▀░█▄▄█░█░▀▄░█░░█░░░█░▀░█
#░▀▀▀░░▀▀░░▀▀░░▀░▀▀░▀░░▀░▀▀▀▀░░▀▀░░░░▀░░▒▀
# Name: Dox?
# Description: Your Best doxing tool!
# Author: @nnllv0y
# ---------------------------------------------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# Author: @nnllv0y
# Commands: gb, deanon, dox
# scope: hikka_only
# meta developer: @nnllv0y
# ---------------------------------------------------------------------------------

__version__ = (1, 0, 1)

from telethon.tl.types import Message # type: ignore
from .. import loader, utils
import asyncio, random

@loader.tds
class dox(loader.Module):
    """Maybe... doxing tool?"""
    
    strings = {
        "name": "DoxTool",
        "gb_1": "Поиск родителей...",
        "gb_2": "Поиск адресов...",
        "gb_3": "Поиск данных пользователя...",
        "gb_4": "Поиск Школы и его класса...",
        "gb_5": "Поиск работы родителей...",
        "gb_r": "Информация о нём!\n\n├ Телефон: разъебанный \n├ Страна: обычная \n├ Регион: пиздоболов \n├ Родители : не ебу\n├ Адрес: Гаваи \n├ Имя: Кто он?\n├ Отчество: отсутствует \n├ Фамилия: отсутствует \n├ Сколько раз ебали в дырку: 32\n├ Пол: ленолиум \n├ Дом : Малдивы \n├ сосёт в день: 20 (раз) за 1000000 руб\n├ больница : №3 \n├ Статус: Хароший \n├ Простата: массирована\n├Рот: выебан\n└ #####################\n\nМать : Лучшая \nместо работы матери: Бизнес\nСтрана: \nсостоящаяся в снггород: я ебу? \nродилась: в имбовой семье\n\nОтец: лучший \nместо работы: Бизнес \nСтрана: состоящаяся в снггород: я ебу?\nродился: Малдивы\nЭто все ШУТКА приват модуль @nnllv0y",
        "info": "Пон",
        "dox_1": "Докс тул активирован",
        "dox_2": "Инфа о нём: 10%",
        "dox_3": "Инфа о нём: 16%",
        "dox_4": "Инфа о нём: 24%",
        "dox_5": "Инфа о нём: 25%",
        "dox_6": "Инфа о нём: 32%",
        "dox_7": "Инфа о нём: 37%",
        "dox_8": "Инфа о нём: 47%",
        "dox_9": "Инфа о нём: 69%",
        "dox_10": "Инфа о нём: 78%",
        "dox_11": "Инфа о нём: 86%",
        "dox_12": "Инфа о нём: 97%",
        "dox_13": "Инфа о нём: 99%",
        "dox_14": "Инфа о нём: 100%",
        "dox_15": "Выдаю информацию...",
        "dox_16": "Информация о нём!\n\n├ Телефон: разъебанный \n├ Страна: обычная \n├ Регион: пиздоболов \n├ Родители : не ебу\n├ Адрес: Где он? \n├ Имя: Кто он?\n├ Отчество: чего? \n├ Фамилия: каво? \n├ Сколько раз ебали в дырку: 1488\n├ Пол: ленолиум \n├ Дом : я типо видел? \n├ Тип: скороупа\n├ больница : №3 \n├ Статус: Не Авторитет \n├ Простата: массирована\n├Рот: выебан\n└ Докс by Глаз боб vip+"
        
     }
    
    async def gbcmd(self, message):
        """search in databases eye of god!"""
        await utils.answer(message, self.strings["gb_1"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_2"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_3"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_4"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_5"])
        await asyncio.sleep(1)
        await message.edit(self.strings["gb_r"])

    async def deanoncmd(self, message):
        """Full information of user in global database"""
        deanon = ["It's bad to do something like this...","I’m tired of you!", "One more prank like this and I’ll delete your account.", "Didn’t you understand the first time?", "Why do you keep doing this??", "We both know that this doesn’t do us any good.", "what won't it lead to?"]
        await utils.answer(message, random.choice(deanon))

    async def dinfocmd(self, message):
        """info of module"""
        await utils.answer(message, self.strings["info"])
        
    async def doxcmd(self, message):
        """Dox"""
        await utils.answer(message, self.strings["dox_1"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_2"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_3"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_4"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_5"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_6"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_7"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_8"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_9"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_10"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_11"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_12"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_13"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_14"])
        await asyncio.sleep(1)
        await message.edit(self.strings["dox_15"])
        await asyncio.sleep(3)
        await message.edit(self.strings["dox_16"])