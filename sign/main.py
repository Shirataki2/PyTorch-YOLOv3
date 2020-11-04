from PIL import Image
from glob import glob
import csv

with open('anno.csv') as f:
    reader = csv.reader(f)
    lines = [row for row in reader]

for line in lines[1:]:
    fp, lbl, *coord = line
    x1, y1, x2, y2 = tuple(map(int, coord))
    img = Image.open(fp.split('/')[-1])
    imgH = img.height    
    imgW = img.width    
    h = (y2 - y1) / imgH
    w = (x2 - x1) / imgW
    cx = (x1 + x2) / (2 * imgW)
    cy = (y1 + y2) / (2 * imgH)
    if lbl == 'Hazard':
        idx = 0
    if lbl == 'Infectious':
        idx = 1
    if lbl == 'Toxic':
        idx = 2
    with open(f'../data/custom/labels/{fp.replace(".jpg", "")}.txt', 'w') as f:
        f.write(' '.join(map(str, [idx, cx, cy, w, h])))
