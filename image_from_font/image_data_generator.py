
# To run
# python image_data_generator.py 0 # for validation
# python image_data_generator.py 1 # for training

import os
import random
from PIL import Image,ImageDraw,ImageFont 




import sys


num_chars = 6

height_norm = 36
width_norm = 100

str_dot_img_ext = '.png'

alphabet = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabet += ''',./<>?;':"[]\{}-=_+~!@#$%^&*()
            '''.replace('space','').strip()


#
# change this value to change the default purpose of data-generating
#
data_for_training = 0                # 1 for training, 0 for test  
# 



#
if len(sys.argv) >= 2:
    #
    data_for_training = int(sys.argv[1])
    #
    if data_for_training != 0 and data_for_training != 1:
        print('The parameter should be 0 or 1.')
        print('Set to 0 by default.')
        data_for_training = 0
        #

#
if data_for_training > 0:
    dir_data_generated = './data_generated'
    NumImages = 50000
else:
    dir_data_generated = './data_test'
    NumImages = 1000
#


#
list_fonts = ['fonts/tecnico_bold.ttf',
              'fonts/tecnico_bolditalic.ttf',
              'fonts/tecnico_regular.ttf']
#             
# list_sizes = [26, 28, 30, 31, 32, 33, 34, 36, 40]
#

#
dir_images_gen = dir_data_generated + '/images'
dir_contents_gen = dir_data_generated + '/contents'
#

#
if not os.path.exists(dir_data_generated): os.mkdir(dir_data_generated)
if not os.path.exists(dir_images_gen): os.mkdir(dir_images_gen)
if not os.path.exists(dir_contents_gen): os.mkdir(dir_contents_gen)
#

#
xs = 3
ys = 3
#
for count in range(NumImages):
    #
    count += 1
    #
    print('current: %d / %d' % (count, NumImages) )
    #
    img_draw = Image.new('RGB', (1000, 1000), (255,255,255))
    #
    draw = ImageDraw.Draw(img_draw)
    #
    # Randomly select Text
    #
    text_str = ''
    i_char = 0
    while i_char < num_chars:
        #
        c = random.choice(alphabet)
        #print(c + ', ' + str(len(c)))
        #
        #if c == ' ': continue
        #
        text_str += c
        i_char += 1
        #
    #
    # Font
    #
    font_file = random.choice(list_fonts)
    #
    text_size = 40
    xe = 2000
    ye = 60
    #
    while xe > width_norm or ye > height_norm:
        #
        text_size -= 1
        font = ImageFont.truetype(font_file, text_size)
        #
        # font size
        tw,th = draw.textsize(text_str,font)
        #
        xe = xs + tw
        ye = ys + th
        #
    #
    # Draw text, set text position/content/color/font
    draw.text((xs,ys), text_str, (0, 0, 0), font=font) 
    #
    # delete brush
    del draw
    #
    #standard size of images
    rect = img_draw.crop([0, 0, width_norm, height_norm])
    #
    #save image
    imageFile = os.path.join(dir_images_gen, str(count) + str_dot_img_ext)
    rect.save(imageFile)
    #
    #save content
    contentFile = os.path.join(dir_contents_gen, str(count) + '.txt')
    with open(contentFile, 'w') as fp:
        fp.write('%d-%d-%d-%d|%s\n' % (xs,ys,xe,ye,text_str) )
        #
    #
    
    
