import keyboard
import time
import pyperclip

print ("Press the ESC key to exit.")
print ("Shortcut: Ctrl + Shift + v")
def type_clipboard():
    clipboard_text = pyperclip.paste()
    print ("Clipboard entry obtained:" + clipboard_text)
    keyboard.write(clipboard_text)
    print ("Typing entry:" + clipboard_text)
    time.sleep(0.2)  # Adjust the delay if needed

keyboard.add_hotkey("ctrl+shift+v", type_clipboard)
keyboard.wait('esc')  # Press Esc to stop the script
