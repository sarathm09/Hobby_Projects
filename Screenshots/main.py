__author__ = 'T90'
__version__ = '1.0.0'

import pyscreenshot as ImageGrab

# fullscreen
im = ImageGrab.grab()
im.show()

# part of the screen
im = ImageGrab.grab(bbox=(10, 10, 500, 500))
im.show()

# to file
ImageGrab.grab_to_file('im.png')