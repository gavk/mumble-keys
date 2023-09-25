#!/usr/bin/env python
"""
Авторы mumble пока не осилили перехват клавиш под wayland,
поэтому пришлось городить этот скрипт.
Скрипту для работы нужны права root.
Если у вашего пользователя UID не 1000,
измените значение переменной XDG_RUNTIME_DIR.
"""
import subprocess
import keyboard
import os
import re


KEY_PRESSED = False
KEY_NAME = 'menu'
XDG_RUNTIME_DIR = '/run/user/1000'


def on_press(key):
    global KEY_PRESSED
    if not KEY_PRESSED:
        if key.name == KEY_NAME:
            KEY_PRESSED = True
            os.system(f'XDG_RUNTIME_DIR={XDG_RUNTIME_DIR} mumble rpc starttalking')


def on_release(key):
    global KEY_PRESSED
    if key.name == KEY_NAME:
        KEY_PRESSED = False
        os.system(f'XDG_RUNTIME_DIR={XDG_RUNTIME_DIR} mumble rpc stoptalking')


if __name__ == '__main__':
    basename = os.path.basename(__file__)
    result = subprocess.run([f'ps', 'ax'], stdout=subprocess.PIPE)
    processes = re.findall(f'{basename}', f'{result.stdout}', flags=re.MULTILINE)
    print(f'processes = {processes}')
    count_processes = len(processes)
    if count_processes > 2:
        print(f'Running other {basename}. Exiting.')
        exit(0)

    keyboard.on_press(on_press)
    keyboard.on_release(on_release, suppress=True)
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        exit(1)
