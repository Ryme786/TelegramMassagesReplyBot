import asyncio
from pyrogram import Client, filters

# Replace with your own values
api_id = '19259149'
api_hash = '67e9ed15eb0adf9d3b391311933fa594'
group_id = -1002263131759  # Replace with the actual group ID

app = Client("6705657501", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(group_id) & ~filters.me)
async def process_message(client, message):
    try:
        text = message.text.lower()
        if text in ['hi', 'hello']:
            sent_message = await message.reply("Hello there, welcome to community.")
            print(f"Message sent successfully: {sent_message.text}")
    except Exception as e:
        print(f"Failed to send message: {e}")

async def main():
    try:
        await app.start()
        print("Bot started")
        # Keep the bot running
        while True:
            await asyncio.sleep(10)
    except Exception as e:
        print(f"Error starting bot: {e}")
    finally:
        await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
