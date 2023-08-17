import time
import pyperclip
import keyboard
import pyautogui

print("Press the ESC key to exit.")
print("Shortcut: Insert")

def type_character(char):
    """Types a character using pyautogui."""
    try:
        print(f"Typing character: {char} using pyautogui")
        pyautogui.write(char)
    except Exception as e:
        print(f"Error typing character {char}: {e}.")

def type_clipboard():
    try:
        clipboard_text = pyperclip.paste()

        # Ensure clipboard contents aren't empty
        assert len(clipboard_text) > 0, "Clipboard is empty!"

        print("Clipboard entry obtained:" + clipboard_text)

        for char in clipboard_text:
            type_character(char)
            time.sleep(0.05)  # adjust this delay if needed

        print("Finished typing clipboard contents.")
        time.sleep(0.2)  # Adjust the delay if needed

    except AssertionError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

keyboard.add_hotkey("ins", type_clipboard)
keyboard.wait('esc')  # Press Esc to stop the script
