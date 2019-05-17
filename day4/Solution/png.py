# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:35:00 2019

@author: user
"""





import os
from PIL import Image

for f in os.listdir('.') :
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, text = os.path.splittext(f)
        i.save('pngs/{}.png'.format(fn))

size_300 = (300,300)
size_700 = (700,700)


for f in os.listdir('.') :
    if f.endswith('.jpg'):
        i = Image.open(f)
        fn, fext = os.path.splittext(f)
        i.thumbnail(size_700)
        i.save('700/{}_700{}'.format(fn,fext))
 
        i.thumbnail(size_300)
        i.save('300/{}_300{}'.format(fn,fext))
 