# LUBRJ(Nina)

name = "test"

import shlex
import os 
import threading
import ctypes
import time
import ctypes
import os
import asset_commands
import asset_commands.banner
uwuhentai = os.getlogin()

available_commands = [f.replace(".py", "") for f in os.listdir("commands") if f.endswith(".py")]

kernel32 = ctypes.WinDLL("kernel32")
user32 = ctypes.WinDLL("user32")

hWnd = kernel32.GetConsoleWindow()

GWL_STYLE = -16
WS_SIZEBOX = 0x00040000
WS_MAXIMIZEBOX = 0x00010000 

style = user32.GetWindowLongW(hWnd, GWL_STYLE)

style &= ~WS_SIZEBOX
style &= ~WS_MAXIMIZEBOX

user32.SetWindowLongW(hWnd, GWL_STYLE, style)
user32.SetWindowPos(hWnd, None, 0, 0, 0, 0,
    0x0002 | 0x0001 | 0x0020)

def termianl():
    while True:
        try:
            print(f"\n┌──{uwuhentai}")
            command = shlex.split(input("└─>"))
            print()
            if not command:
                continue

            cmd_name = command[0].lower()
            args = command[1:]

            if cmd_name in available_commands:
                try:
                    module = __import__(f"commands.{cmd_name}", fromlist=["command"])
                    module.command(*args)
                except Exception as e:
                    print(f"error: {e}")
            else:
                print(f"no command with the name: '{cmd_name}' found")
        except KeyboardInterrupt:
            print("use 'exit' instead")

def titlespammer():
    word = f"   {name}           "
    while True:
        for i in range(len(word)):
            shifted_word = word[i:] + word[:i]
            ctypes.windll.kernel32.SetConsoleTitleW(shifted_word)
            time.sleep(0.1)

title_thread = threading.Thread(target=titlespammer, daemon=True)
title_thread.start()

asset_commands.banner.banner()

termianl()
