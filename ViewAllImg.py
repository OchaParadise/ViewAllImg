#! usr/bin/python
#coding: UTF-8

import os
import hashlib
import sys

# mediawikiディレクトリの画像の一覧のhtmlファイル生成

def wrapInHtml(body, htmlName):
    htmlfile = open(htmlName, 'w')
    htmlobj = """<html>
                 <head></head>
                 <body> %s </body>
                 </html>""" % body

    htmlfile.write(htmlobj)
    htmlfile.close    

def joinString(string, obj):
    string = string + obj + '<br>'
    return string

def toHash(imgName):
    hashnum = hashlib.md5(imgName).hexdigest()
    return hashnum[:2]

def makePath(dirhash, filename):
    path = '/var/www/mediawiki-1.18.1/image/' + str(dirhash[:1]) + '/' + str(dirhash[:2]) + '/' + filename
    return path

def makeImageTag(imgPath):
    path = '<img src = "%s"> <br>' % imgPath
    return path

def main():
    imagePathList = ''

    for i in range(int(sys.argv[1])):
        imageFile = 'n' + str(i).zfill(6) + '.JPG'
        imageHash = toHash(imageFile)
        imagePath = makePath(imageHash, imageFile)
        imageTag = makeImageTag(imagePath)
        imagePathList = joinString(imagePathList, imageTag)
        if i % 10 == 0 and i != 0:
            wrapInHtml(imagePathList, 'hello%s.html' % str(i/10))
            imagePathList = ''
    
    if imagePathList != '':
        wrapInHtml(imagePathList, 'hello%s.html' % str(i/10+1))


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit('Frror: No argv')
    main()
