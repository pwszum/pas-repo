#!/usr/bin/env python3
import shutil

print('Filename to copy: ', end='')
src = input() + '.png'
dst = 'lab1zad1.png'

try:
    shutil.copyfile(src, dst)
    print('File copied successfully')
except FileNotFoundError:
    print('File not found')
except:
    print('Error')
