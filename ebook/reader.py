# -*- coding: utf-8 -*
from ebook_reader import *
import sys
import keyboard
import os

def hide():
    os.system('cls')
    print('Focus! Focus! Focus on your fantastic work my little baby!')

def initialize():
    os.system('cls')
    print('\nLoading...')
    show_chapter()
    daily_help()

def next_chapter():
    os.system('cls')
    print('\nLoading...')
    goto_next()
    show_chapter()
    daily_help()

def prev_chapter():
    os.system('cls')
    print('\nLoading...')
    goto_prev()
    show_chapter()
    daily_help()

def daily_help():
    print('\nPress crtl+c for quit.\nPress \'h\' for more help.\n')

def more_help():
    print('\nPress right for next chapter.\nPress left for previous chapter.')
    print('Press up for hide the reader.\nPress down to reload current chapter.')
    print('Press \'t\'for test function.\n')

def test():
    print('Func for test...')

if __name__ == "__main__":
    initialize()
    keyboard.add_hotkey('t', test)
    keyboard.add_hotkey('h', more_help)
    keyboard.add_hotkey('left', prev_chapter)
    keyboard.add_hotkey('right', next_chapter)
    keyboard.add_hotkey('up', hide)
    keyboard.add_hotkey('down', initialize)
    keyboard.wait()