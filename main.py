from datetime import datetime
from re import I
from pyrogram import Client, filters
import asyncio
from pyrogram.errors import FloodWait
import os
import time

os.environ["TZ"] = "Asia/Colombo"
time.tzset()


bot = Client(
    'MY first project',
    api_id=7009965,
    api_hash="06651b174c4f0591deb0ed1e5663c996",
    bot_token="5334604290:AAHHLFPT9Aqd76D8d41I6_0VsYhlamDYh8o"
    
)

stoptimer = False

@bot.on_message(filters.command('al'))
async def set_timer(bot, message):
    global stoptimer
    try:
            dt1 = datetime.now()
            dt2 = datetime(2022,12,5,00,00,00)
            dt3 = int((dt2 - dt1).total_seconds())
            user_input_time = dt3
            user_input_event = str("🔥🔥උසස් පෙළ විභාගයට තව🔥🔥")
            get_user_input_time = await bot.send_message(message.chat.id, user_input_time)
            await get_user_input_time.pin()
            if stoptimer: stoptimer = False
            if 0<user_input_time<=10 :
                while user_input_time and not stoptimer:
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ **තත්පර** {:02d}**ක** කාලයක් තිබෙයි. 📚\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs\n\n '.format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(1)
                    user_input_time -=1
            elif 10<user_input_time<60:
                while user_input_time>0 and not stoptimer:
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ **තත්පර** {:02d}**ක** කාලයක් තිබෙයි. 📚\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs\n\n '.format(user_input_event, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif 60<=user_input_time<3600:
                while user_input_time>0 and not stoptimer:
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ **මිනිත්තු** {:02d}**යි**  **තත්පර** {:02d}**ක** කාලයක් තිබෙයි. 📚\n\n<i>"Your **Time** Is Limited, So Don\'t Waste It Living Someone Else\'s Life"</i>\n      - Steve Jobs\n\n '.format(user_input_event, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(3)
                    user_input_time -=3
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif 3600<=user_input_time<86400:
                while user_input_time>0 and not stoptimer:
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60

                    Countdown_TeLe_TiPs='{}\n\n⏳ **පැය** {:02d}**යි**  **මිනිත්තු** {:02d}**යි** **තත්පර** {:02d}**ක** කාලයක් තිබෙයි. 📚\n\n<i>"ඔබ තවමත් ප්‍රමාද නැත"</i>\n\nPowered By '.format(user_input_event, h, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(7)
                    user_input_time -=7
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            elif user_input_time>=86400:
                while user_input_time>0 and not stoptimer:
                    d=user_input_time//(3600*24)
                    h=user_input_time%(3600*24)//3600
                    m=user_input_time%3600//60
                    s=user_input_time%60
                    Countdown_TeLe_TiPs='{}\n\n⏳ **දින** {:02d}**යි**  **පැය** {:02d}**යි**  **මිනිත්තු** {:02d}**යි** **තත්පර** {:02d}  **ක** කාලයක් තිබෙයි. 📚\n\n<i>"ඔබ තවමත් ප්‍රමාද නැත"</i>\n\nPowered By '.format(user_input_event, d, h, m, s)
                    finish_countdown = await get_user_input_time.edit(Countdown_TeLe_TiPs)
                    await asyncio.sleep(9)
                    user_input_time -=9
                await finish_countdown.edit("🚨 Beep! Beep!! **TIME'S UP!!!**")
            else:
                await get_user_input_time.edit(f"🤷🏻‍♂️ I can't countdown from {user_input_time}")
                
    except FloodWait as e:
        await asyncio.sleep(e.x)
@bot.on_message(filters.command('stopc'))
async def stop_timer(bot, message):
    global stoptimer
    try:
        if (await bot.get_chat_member(message.chat.id,message.from_user.id)):
            stoptimer = True
            await message.reply('🛑 Countdown stopped.')
        else:
            await message.reply('👮🏻‍♂️ Sorry, **only admins** can execute this command.')
    except FloodWait as e:
        await asyncio.sleep(e.x) 
bot.run()
