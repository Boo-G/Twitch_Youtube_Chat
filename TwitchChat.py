import socket
import logging
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s — %(message)s',
                    datefmt='%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])


"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'Hsboog'
token = os.getenv('TWITCH_API_KEY')
channel = '#esfandtv'


def main(twitchChat):
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {str(twitchChat)}\r\n".encode('utf-8'))

    try:
        while True:
            resp = sock.recv(2048).decode('utf-8')
            # print(resp)

            if resp.startswith('PING'):
                # sock.send("PONG :tmi.twitch.tv\n".encode('utf-8'))
                sock.send("PONG\n".encode('utf-8'))
            elif len(resp) > 0:
                # print(resp)
                # logging.info(demojize(resp))

                # Check if the response contains the PRIVMSG format
                if "PRIVMSG" in resp:
                
                    # Extract the message and time from the response
                    parts = resp.split(":", 2)
                    user = parts[1].split("!", 1)[0]
                    message = parts[2].strip()
                    time_received = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Log the message with the configured logger
                    print(f"TWITCH | {user}: {message}")
                    logging.info(f"TWITCH | {user}: {message}")


    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()