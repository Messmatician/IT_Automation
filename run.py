#! /usr/bin/env python3
import os
import requests
import json
import re

dir = "/home/student-04-39b239d0c098/supplier-data/descriptions/"
for txt in os.listdir(dir):
  if txt.endswith(".txt"):
    dic = {}
    with open(dir + txt) as f:
      dic['name'] = f.readline()
      weight = int(re.match("[0-9]*", f.readline()).groups()[0])
      print(weight)
      dic['weight'] = weight
      dic['description'] = f.readline()
      dic['mage_name'] = txt - '.txt' + '.jpeg'
    print(dic)

