import asyncio
import edge_tts

async def main():
    communicate = edge_tts.Communicate(
        text="Hello Anirudh. I am Friday. How can I help you today?",
        voice="en-US-GuyNeural"
    )

    await communicate.save("voice.mp3")

asyncio.run(main())