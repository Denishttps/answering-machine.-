from pyrogram import Client, filters
from config import api_hash, api_id, ctg
from DB import DB
import logging
from run import keep_alive

app = Client("sleepbot", api_hash=api_hash, api_id=api_id)
db = DB()
logging.basicConfig(level=logging.INFO)


@app.on_message(filters.command(commands=["afk"], prefixes=".",) & filters.me)
async def on_afk(client, msg):
  get = db.get_status(ctg)
  if get:
    db.del_process()
    db.del_status("True")
    await msg.edit_text("I'm not afk anymore")
  else:
    db.status(msg.from_user.id, "True", msg.text[4:])
    await msg.edit_text("I'm AFK right now!")
    

@app.on_message(filters.private)
async def slpbot(client, msg):
  get_status = db.get_status(ctg)
  if get_status:
    if not db.get_proc(msg.from_user.id):
      await app.send_message(msg.chat.id, "I'm AFK right now!\nReason: "+str(get_status[2]))
      db.processed(msg.from_user.id)
      

if __name__ == "__main__":
  print("Bot started")
  keep_alive()
  app.run()

