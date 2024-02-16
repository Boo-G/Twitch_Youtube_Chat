import socket
import logging
from emoji import demojize
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])


"""
Get token here: https://twitchapps.com/tmi/
"""

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'Hsboog'
token = 'oauth:yni8ods6axw67z3q7ovrgbgkqq2axs'
channel = '#esfandtv'


def main():
    sock = socket.socket()
    sock.connect((server, port))
    sock.send(f"PASS {token}\r\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\r\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\r\n".encode('utf-8'))

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
                    logging.info(f"TWITCH | {time_received} | {user}: {message}")


    except KeyboardInterrupt:
        sock.close()
        exit()

if __name__ == '__main__':
    main()