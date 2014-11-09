__author__ = 'T90'
__version__ = '1.0.0'

from subprocess import call
import os

a = os.popen("bcc32 a.c").read()

print a

