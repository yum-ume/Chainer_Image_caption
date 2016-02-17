#coding: utf-8
import sys
import string

fr1 = open(sys.argv[1],"r")
fr2 = open(sys.argv[2])
fw = open(sys.argv[3], "w")

img_name=fr2.read()
#print img_name
names=img_name.split("\n")

for l in fr1:
    l = l.strip()
    file, catID= l.split(" ")
    if not file in names:
        #print file_name
        fw.write(l+"\n")

