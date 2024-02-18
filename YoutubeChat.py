import pytchat
import logging

# Set the logging level for httpx to WARNING
logging.getLogger("httpx").setLevel(logging.WARNING)

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

chat = pytchat.create(video_id="4xDzrJKXOOY")

while chat.is_alive():
    for c in chat.get().sync_items():
        # print(f"YOUTUBE | {c.datetime} | {c.author.name}: {c.message}")
        logging.info(f"YOUTUBE | {c.datetime} | {c.author.name}: {c.message}")

    # for c in chat.get().items:
    #     print(c.json())


