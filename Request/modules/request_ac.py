# -----------CREDITS -----------
# telegram : @legend_coder
# github : noob-mukesh
from pyrogram import filters
import asyncio,os
from .. import Mukesh
from pyrogram.enums import ParseMode
from pyrogram.types import ChatJoinRequest,InlineKeyboardButton,InlineKeyboardMarkup
from pytz import timezone 
from datetime import datetime
from config import *
from pyrogram import enums

@Mukesh.on_chat_join_request(filters.group | filters.channel)
async def join_requests(client: Mukesh, msg: ChatJoinRequest):
    try:
        ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
        user_id = msg.from_user.id
        chat_id = msg.chat.id
        print(user_id,chat_id)

        # Verify if the chat_id is valid before proceeding
        if chat_id not in ALL_CHAT:
            print(ALL_CHAT)
            return False

        # Fetch chat members, considering the potential invalid peer ID
        try:
            members = [m.user.id async for m in client.get_chat_members(MAIN_CHAT_ID)]
            # count = await client.get_chat_members_count(MAIN_CHAT_ID)
            # print(count)
            # print(members)
        except ValueError as ve:
            print(f"Error fetching chat members: {ve}")
            return 

        # Check if the user is a member of the chat
        if user_id not in members:
            await client.decline_chat_join_request(chat_id, user_id)
            return await client.send_message(user_id, f"ʜᴇʟʟᴏ {msg.from_user.mention} \nYour Request Channel {msg.chat.title} \n\n🚀 Welcome!
📢 Channel shift થયો છે
⚠️ Copyright આવે તો link આ bot માં મળશે
❌ Bot delete કરશો નહીં 💯",
                              reply_markup=InlineKeyboardMarkup([
                                  [InlineKeyboardButton("Join Now", url="https://t.me/+ySXWdGOMpfJmM2M5")]
                              ]))
        if APPROVED == "on":
            # Approve the user's chat join request
            await client.approve_chat_join_request(chat_id, user_id)
            # Send a welcome message, including the user's join details
            join_message = f"​ʜᴇʟʟᴏ {msg.from_user.mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {msg.chat.title}\nᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time}\n\nʏᴏᴜ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {Mukesh.mention} \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ  @ASPIRANT_HELPSBOT\n\nHello dost , hu parth pandya કય કામ હોય તો [ @ASPIRANT_HELPSBOT ] આમાં મેસેજ કરી દેજો નવરો થઈ રિપ્લે આપી દેય ✨ “જે બીજાની મદદ કરે છે, તેની મદદ ભગવાન કરે છે.”===\n❤️Thank You❤️"

            await client.send_message(user_id, join_message)
    except Exception as e:
        print(f"An error occurred: {e}")
# async def join_requests(client: Mukesh, msg: ChatJoinRequest):
#     ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')
#     user_id = msg.from_user.id
#     chat_id = msg.chat.id
#     # CHECK ALL CHAT
#     if chat_id not in ALL_CHAT:
#         return
#     members=[]
#     async for m in client.get_chat_members(-1002157881101):
#         members.append(m.user.id)
        
#     #  CHECK ALL MEMBER
#     if user_id  not in members:
#         return    
    
#     try:
#         #  APPROVE THEM
#         await client.approve_chat_join_request(chat_id, user_id)
#         if APPROVED == "on":
#             chat_photo = msg.chat.photo.big_file_id 
#             if chat_photo:
#                 #  SEND  IMG +MSG  AFTER JOINING
#                 img=await client.download_media(chat_photo)
#                 await client.send_photo(
#                     chat_id=user_id,photo=img,
#                     caption=f"​ʜᴇʟʟᴏ {msg.from_user.mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {msg.chat.title}  \nᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time}\n\nʏᴏᴜ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {Mukesh.mention} \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ  ||@sarkari_student||\n\nHello dost , mai aapka sarkari student bot aap hamare bot delete na karna sabhi premium members ki update , and sabhi information hamare bot par milegi ===\n❤️Thank You❤️",
#                     )
#             else:
#                 #  SEND MSG AFTER JOINING
#                 await client.send_message(
#                     user_id,f"​ʜᴇʟʟᴏ {msg.from_user.mention}\nᴡᴇʟᴄᴏᴍᴇ ᴛᴏ {msg.chat.title}  \nᴊᴏɪɴᴇᴅ ᴀᴛ: {ind_time}\n\nʏᴏᴜ ᴀᴘᴘʀᴏᴠᴇᴅ ʙʏ {Mukesh.mention} \n\nᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ  ||@sarkari_student||\n\nHello dost , mai aapka sarkari student bot aap hamare bot delete na karna sabhi premium members ki update , and sabhi information hamare bot par milegi ===\n❤️Thank You❤️",
#                     )
#     except Exception as E:
#         print(E)
