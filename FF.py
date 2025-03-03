import discord
import asyncio
import random
from discord.ext import commands
from dotenv import load_dotenv
import os
from flask import Flask
from threading import Thread

discord.Intents.default()
load_dotenv()

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("TOKEN is missing. Please check your .env file.")
    exit()

# ตั้งค่า intents ให้บอทเห็นสมาชิก และใช้คำสั่งได้
intents = discord.Intents.default()
intents.members = True
intents.message_content = True  # เปิดให้บอทอ่านข้อความได้
bot = commands.Bot(command_prefix="/", intents=intents)

# 📌 ฟังก์ชันทำให้บอทออนไลน์ 24 ชม.
app = Flask('')

@app.route('/')
def home():
    return "บอทยังออนไลน์อยู่!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 📌 เมื่อบอทออนไลน์
@bot.event
async def on_ready():
    print(f'✅ บอทออนไลน์เป็น {bot.user}')    

# 📌 เก็บข้อความที่เคยส่งไปแล้วเพื่อไม่ให้ซ้ำ
sent_messages = {}

# 📌 คำสั่งให้ DM หา "เฉพาะคนที่ระบุ" พร้อมข้อความสุ่มไม่ซ้ำ
@bot.command()
async def dm(ctx, member: discord.Member):
    messages = [
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3669077851","com.garena.msdk.guest_password":"410176797FEB007AC82098960D2171C5A2CBACAB20C8544D77EEAEA98F11777A"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3682286759","com.garena.msdk.guest_password":"8CB9DC14313ECCDB3541004636D9329BAF757BB88A04E146E5060466FD539999F"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3682283822","com.garena.msdk.guest_password":"0A082C4A747BF4F78758787FF709E65F24BAC31930BB331EF8649470FE04C68"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767760177","com.garena.msdk.guest_password":"E81C30476360846E896993CC48B7D4F3204B746F350472A5BF07D01BD0778ECD"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767760167","com.garena.msdk.guest_password":"AA29CB95A95E1840CA86C1DCAAC5CBE7D3A4652B9774377E535A9AA4CB050B12"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767760190","com.garena.msdk.guest_password":"89B96977FEE7B44382717FEE06DA73532F674E3D34733DB68740DF94D9B0E180"}}```'
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767760183","com.garena.msdk.guest_password":"0D900BDD0DFE11796590CF54619803A1755BDCAE37222E6EAE0B7CE2AC349A67"}}```'
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764450","com.garena.msdk.guest_password":"EFF22076794696E7CD8678171A5ABE3AA659615B6C747C9DB2BE2F2B26900740"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764442","com.garena.msdk.guest_password":"1A09DBC7BB1094F33FC482F2346887D0375088DA6F439D329E467263BDC6EF57"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764444","com.garena.msdk.guest_password":"8044FA60F6CFA854EBE10C305316B56962A1DF4139EFF0A9782CA7B91F74C0A7"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767760172","com.garena.msdk.guest_password":"65A0D8557043A6536E3EE6EB4D426B19D8A7895426DC1C50D97556D9D1A92979"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764455","com.garena.msdk.guest_password":"23A1064310E7C45A110917281AB1E68FFAF55C333EC728279E7094D718E2AF0F"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764446","com.garena.msdk.guest_password":"A905D91E1C0429D59123B9AD2DAFC1F9EF1DF69C98E55415027F64E3D0AC3F59"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764449","com.garena.msdk.guest_password":"64B069F099E4A5668E3C2BEBD60C3B24F22A9F9CD09AC0139984D60950409A83"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764454","com.garena.msdk.guest_password":"AE15B7877D9995BF47FCD3B666F7908A180C1EFD597B738E3D06E1E2989B2CF3"}}```',
        'ID Free Fire Code ขอบคุณที่ไว้ใจ +1ได้ที่ https://discord.com/channels/1336730374490820700/1345707058619482144 ```{"guest_account_info":{"com.garena.msdk.guest_uid":"3767764440","com.garena.msdk.guest_password":"DEC0645DE4D35D9474E08EC46E05520341576FE6A549B9936091E76A9A53A4B3"}}```'
    ]
    
    if member.id not in sent_messages:
        sent_messages[member.id] = []
    
    available_messages = list(set(messages) - set(sent_messages[member.id]))
    
    if not available_messages:
        await ctx.author.send(f"⚠️ โค้ดIDหมดรอเติมสต็อก ที่ห้อง https://discord.com/channels/1336730374490820700/1346094257668227122 {member.mention}! กรุณาลองใหม่ภายหลัง!")
        return
    
    message = random.choice(available_messages)
    sent_messages[member.id].append(message)
    
    if member.bot:
        await ctx.message.delete()
        return
    try:
        await member.send(message)
        await ctx.author.send(f"✅ ส่ง DM ให้ {member.mention}")
    except:
        await ctx.author.send(f"❌ ไม่สามารถส่ง DM ให้ {member.mention} ได้!")
    await ctx.message.delete()

# 📌 ทำให้บอทออนไลน์ตลอดเวลา
keep_alive()

# 📌 รันบอท
bot.run(TOKEN)
