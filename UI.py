import tkinter as tk

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

# Create the Tkinter window
root = tk.Tk()
root.title("Latest Chat Messages")


# Create labels and entry widgets for YouTube and Twitch channels
youtube_label = tk.Label(root, text="YouTube Channel:")
youtube_label.pack()
youtube_entry = tk.Entry(root)
youtube_entry.pack()

twitch_label = tk.Label(root, text="Twitch Channel:")
twitch_label.pack()
twitch_entry = tk.Entry(root)
twitch_entry.pack()

# Create a search button to load chat log
search_button = tk.Button(root, text="Search", command=load_latest_messages)
search_button.pack()


# Create a text widget to display the chat messages
chat_text = tk.Text(root)
chat_text.pack()

# Call the function to load latest messages initially
load_latest_messages()

# Start the Tkinter event loop
root.mainloop()

