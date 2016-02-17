from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "."))
from PIL import Image

ImageDir=sys.argv[1]
ResizeImageDir=sys.argv[2]
dataDir ='..'
dataType='val2014'
annFile='%s/annotations/instances_%s.json'%(dataDir,dataType)

# initialize COCO api for instance annotations
coco=COCO(annFile)

# display COCO categories and supercategories
cats = coco.loadCats(coco.getCatIds())
names=[cat['name'] for cat in cats]
ids=[cat['id'] for cat in cats]
name_ids = {}

for i in range(len(names)):
    if ids[i] not in name_ids:
        name_ids.update({names[i]:ids[i]})

# get all images containing given categories, select one at random
img_dict = {}

for name in names:
    catIds = coco.getCatIds(catNms=[name]);
    imgIds = coco.getImgIds(catIds=catIds );
    for i in range(len(imgIds)):
        img = coco.loadImgs(imgIds[i])[0]
        if img["file_name"] not in img_dict:
            img_dict.update({img["file_name"]: name})

for k,v in sorted(img_dict.items(), key=lambda x: x[0]):
    ImageFile = '%s/%s'%(ImageDir,k)
    pil_im = Image.open(ImageFile)
    out = pil_im.resize((255, 255))
    save_image = '%s/%s'%(ResizeImageDir,k)
    out.save(save_image)
    print(save_image + " " + str(name_ids[v]))
