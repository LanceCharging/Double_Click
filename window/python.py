import keyboard, mouse
from pyperclip import paste
from googletrans import Translator
import time

translator = Translator()


def translate_to_korean(word):
    translation = translator.translate(word, src="en", dest="ko")
    return translation.text


def translate_selected_text():
    keyboard.press_and_release("ctrl+c")
    time.sleep(0.1)
    clipboard_content = paste()
    print(f"paste : {clipboard_content}")
    if clipboard_content != "":
        result = translate_to_korean(clipboard_content)
        if result != clipboard_content:
            print(result)
            return result
    print("failed...")
    return "???"


mouse.on_double_click(translate_selected_text)

from keyboard import wait as kwait

kwait("esc")
