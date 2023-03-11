#!/usr/bin/env python3
import shutil

print('Filename to copy: ', end='')
src = input() + '.txt'
dst = 'lab1zad1.txt'

try:
    shutil.copyfile(src, dst)
    print('File copied successfully')
except FileNotFoundError:
    print('File not found')
except:
    print('Error')
