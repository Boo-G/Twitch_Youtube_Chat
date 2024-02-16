import tkinter as tk

def load_latest_messages():
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

# Create a text widget to display the chat messages
chat_text = tk.Text(root)
chat_text.pack()

# Call the function to load latest messages initially
load_latest_messages()

# Start the Tkinter event loop
root.mainloop()

