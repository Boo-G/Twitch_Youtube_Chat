import tkinter as tk
from tkinter import *
import threading, YoutubeChat, TwitchChat




def search_channels():
    twitch_channel = twitch_entry.get()
    youtube_channel = youtube_entry.get()
    print("Searching Twitch channel:", twitch_channel)
    print("Searching YouTube channel:", youtube_channel)

    # if TwitchChat.main(twitch_channel) and YoutubeChat.main(youtube_channel):
    #     do the stuff

    # Create a threads for fetching each chat
    twitch_thread = threading.Thread(target=TwitchChat.main, args=(twitch_channel,))
    twitch_thread.start()

    youtube_thread = threading.Thread(target=YoutubeChat.main, args=(youtube_channel,))
    youtube_thread.start()

    # Wait for the YoutubeChat thread to complete
    # twitch_thread.join()
    

    # Open and display the chat log file
    load_latest_messages()

def load_latest_messages():
    youtube_channel = youtube_entry.get()
    twitch_channel = twitch_entry.get()


    if youtube_channel and twitch_channel:
        # Read the chat log file with specified encoding
        with open('chat.log', 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Extract the latest 20 messages
        latest_messages = lines[-20:]

        # Update the text in the GUI
        chat_text.delete(1.0, tk.END)  # Clear previous text
        chat_text.insert(tk.END, ''.join(latest_messages))

        # Schedule the function to run again after 1 second
        root.after(1000, load_latest_messages)


"""

Search Window

"""
# Create main window
root = tk.Tk()
root.title("Channel Search")
root.geometry("500x700")

# Load background image
background_image = PhotoImage(file="background.png")

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a frame to hold the input fields and button
frame = tk.Frame(root, bg='white')
frame.place(relx=0.5, rely=0.5, anchor='center')

# Create Twitch channel input
twitch_label = tk.Label(frame, text="Twitch Channel:")
twitch_label.grid(row=0, column=0)
twitch_entry = tk.Entry(frame, width=30)
twitch_entry.grid(row=1, column=0)

# Create YouTube channel input
youtube_label = tk.Label(frame, text="YouTube Channel:")
youtube_label.grid(row=2, column=0)
youtube_entry = tk.Entry(frame, width=30)
youtube_entry.grid(row=3, column=0)

# Create search button
search_button = tk.Button(frame, text="Search", command=search_channels)
search_button.grid(row=4, column=0)


"""

Chat window

"""
# Create the live chat window
newWindow = tk.Toplevel(root)
newWindow.title("Live Chat")
newWindow.geometry("500x700")

# Create a text widget to display the chat messages
chat_text = tk.Text(newWindow, height=700, width=500, wrap=tk.WORD, font=("Helvetica", 12))
chat_text.config(foreground="white")
chat_text.config(background="#201c1c")
chat_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
