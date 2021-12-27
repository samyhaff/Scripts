#!/usr/bin/env python

import argparse
from ImageGoNord import GoNord

parser = argparse.ArgumentParser(description='convert image palette to specified palette')
parser.add_argument('colorscheme', type=str, help='name of the colorscheme')
parser.add_argument('image', type=str, help='path to the image')
args = parser.parse_args()

path = "/home/samy/.config/colorschemes/" + args.colorscheme

with open(path, 'r') as f:
    lines = f.readlines()

colors = [line.split()[2] for line in lines]

go_nord = GoNord()
go_nord.reset_palette()
for color in colors:
    go_nord.add_color_to_palette(color)

print(args.image)
image = go_nord.open_image(args.image)
go_nord.convert_image(image, save_path='/home/samy/Wallpapers/wall.png')
