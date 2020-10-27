#!/usr/bin/env python3
from PIL import Image
import os
import os.path

dir = "/home/student-04-39b239d0c098/supplier-data/images"
for image in os.listdir(dir):
  if image.endswith(".tiff"):
    img = Image.open(dir + "/" + image)
    imgname = image.strip(".tiff")
    img.resize((600, 400)).convert("RGB").save(dir + "/" + imgname + ".jpeg", "JPEG")
