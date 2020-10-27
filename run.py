#! /usr/bin/env python3
import os
import requests
import json
import re

url = 'http://35.202.201.153/fruits/'
dir = "/home/student-03-c4490e41965f/supplier-data/descriptions/"
for txt in os.listdir(dir):
  if txt.endswith(".txt"):
    dic = {}
    with open(dir + txt) as f:
      dic['name'] = f.readline()
      weight = int(re.match("[0-9]*", f.readline()).group())
      print(weight)
      dic['weight'] = weight
      dic['description'] = f.readline()
      dic['image_name'] = txt.strip('.txt') + '.jpeg'
    dic_json = json.dumps(dic)
    requests.post(url, json = dic)
