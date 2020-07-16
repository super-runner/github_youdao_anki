#!/usr/bin/python3
# encoding: utf-8

# Note
# This file is created to convert exported xml from youdao to upload into Anki (a vocabulary learning app)

import os
import sys
from ntpath import basename
from lxml import etree as ET

def parseEngine(fpath):
    
    curDir = os.path.dirname(fpath)
    fname, ext = os.path.splitext(basename(fpath))
    
    if curDir == "":
        curDir = os.getcwd()

    if not os.path.exists(fpath):
        print ("File dones not exist!")
        exit(1)

    parser = ET.XMLParser(strip_cdata=True, encoding='utf8')
    root = ET.parse(fpath, parser)

    items = root.findall('item')

    all_words = str()
    for item in items:
        all_words +=  str(item.find('word').text) + ' ' + str(item.find('phonetic').text) + ' ^ '  \
                    + str(item.find('trans').text) + ' ^ ' \
                    + str(item.find('tags').text)
                    
        all_words = all_words.replace("\n","") + '\r\n'
                   
    # Do NOT give extention file name as .xml, otherwise Anki fails to import
    with open(curDir+"/"+fname+'_extracted.txt', 'w', encoding='utf8') as f:
        f.write(all_words)
    
if __name__ == "__main__":
    argNum = len(sys.argv)
    if argNum < 2:
        print ("Enter your xml path!\n")
        exit(1)
    elif argNum > 2:
        print ("Only require ONE argument!\n")
        exit(1)
        
    parseEngine(sys.argv[1])
