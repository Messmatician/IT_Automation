#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
dir = "/home/student-03-c4490e41965f/supplier-data/images"
for image in os.listdir(dir):
  if image.endswith(".jpeg"):
    with open(dir + "/" + image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
