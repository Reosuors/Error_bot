import os
import discord
from dotenv import load_dotenv

load_dotenv()

# إعداد الصلاحيات
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# ------------------- [ المعرفات IDs ] -------------------
VALUE_CHANNEL_ID = 1336771401236602930
VALUE_BOT_ID = 107395052914056074
STORE_CHANNEL_ID = 0  # ⚠️ حط ID روم المتجر هون

# ------------------- [ كليشة الفاليو ] -------------------
REPLY_MESSAGE = """╭─── 💡 **معرفة أسعار الفواكه والجيم باسات** ───╮

> 📌 **تقدر تفحص قيمة أي فاكهة أو جيم باس بنفسك!**
> استخدم الأمر التفاعلي: `/value`

`1` اكتب `/value` بالشات هنا.
`2` اختار الفاكهة أو الجيم باس (Gamepass) من القائمة.

╰────────────────────────────────────╯"""

@client.event
async def on_ready():
    print(f'✅ البوت يعمل بنجاح باسم: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # قسم الفاليو
    if message.channel.id == VALUE_CHANNEL_ID and message.author.id == VALUE_BOT_ID:
        await message.channel.send(REPLY_MESSAGE)

    # قسم المتجر
    if message.channel.id == STORE_CHANNEL_ID:
        try:
            await message.add_reaction('🇼')
            await message.add_reaction('🇱')
        except Exception as e:
            print(f"خطأ أثناء إضافة التفاعلات: {e}")

client.run(os.getenv("DISCORD_TOKEN"))
