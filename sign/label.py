from PIL import Image
from glob import glob
import csv

with open('anno.csv') as f:
    reader = csv.reader(f)
    lines = [row for row in reader]

for line in lines[1:]:
    fp, *rest = line
    print('data/custom/images/'+fp)