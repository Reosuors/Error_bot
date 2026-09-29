import discord

# إعداد الصلاحيات
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# ------------------- [ المعرفات IDs ] -------------------
VALUE_CHANNEL_ID = 1536711401236602930    # ID روم الفاليو
VALUE_BOT_ID = 1073950529140568074        # ID بوت الفاليو
STORE_CHANNEL_ID = 1548083461859049602    # ⚠️ ايمسح هذا الرقم وضَع ID روم المتجر الخاص بك

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
    # تجاهل رسائل البوت نفسه
    if message.author == client.user:
        return

    # 1️⃣ قسم الفاليو: الرد المباشر بعد بوت الفاليو
    if message.channel.id == VALUE_CHANNEL_ID and message.author.id == VALUE_BOT_ID:
        await message.channel.send(REPLY_MESSAGE)

    # 2️⃣ قسم المتجر: إضافة تفاعلات W و L تلقائياً على كل رسالة
    if message.channel.id == STORE_CHANNEL_ID:
        try:
            await message.add_reaction('🇼')
            await message.add_reaction('🇱')
        except Exception as e:
            print(f"خطأ أثناء إضافة التفاعلات: {e}")

# ⚠️ ضع التوكن الجديد الذي نسخته من Developer Portal بين الكوتيشن
client.run('MTU1NDU1NDU4MzI5NTE5NzM4Nw.GEvJkm.CGb8E3bpR1-Y_xd694R5c4Y8NbGNYLzoIRWIGk')
