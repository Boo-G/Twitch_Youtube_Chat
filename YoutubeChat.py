import pytchat
import time
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

chat = pytchat.create(video_id="1MvwYMZZc_0")

while chat.is_alive():
    for c in chat.get().sync_items():
        print(f"YOUTUBE | {c.datetime} | {c.author.name}: {c.message}")
