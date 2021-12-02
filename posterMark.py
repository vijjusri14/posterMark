# -*- coding: utf-8 -*-
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

settings = json.load(open("settings.json"))
fileList = json.load(open("fileList.json"))

titlePosition = eval(settings["Title"]["Position"])
titleColor = eval(settings["Title"]["Color"])
titleFontSize = settings["Title"]["Size"]
titleFontPath = os.path.join(settings["FontsPath"], settings["Title"]["Font"])
titleFont = ImageFont.truetype(titleFontPath, titleFontSize)

subtitlePosition = eval(settings["Subtitle"]["Position"])
subtitleColor = eval(settings["Subtitle"]["Color"])
subtitleFontSize = settings["Subtitle"]["Size"]
subtitleFontPath = os.path.join(
    settings["FontsPath"], settings["Subtitle"]["Font"])
subtitleFont = ImageFont.truetype(subtitleFontPath, subtitleFontSize)

posterIn = os.path.join(settings["ImagesPath"], settings["BackgroundImage"])
outDir = settings["OutputPath"]

spacer = u"═════════════════════════════════════════════════════════════"


def make_posters():
    "Initialized making posters..."
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    print(spacer)
    for fileName, fileText in fileList.items():
        try:
            img = Image.open(posterIn)
            draw = ImageDraw.Draw(img)
            titleText = fileText["Title"]
            subtitleText = fileText["Subtitle"]
            draw.text(titlePosition, titleText, titleColor, font=titleFont)
            draw.text(subtitlePosition, subtitleText,
                      subtitleColor, font=subtitleFont)
            posterOut = os.path.join(outDir, fileName + ".png")
            img.save(posterOut)
            print("Render status:\033[1;32;40m Success \033[1;37;40m \nName: %s" % fileName,
                  "\nType: %s" % img.format, "\nSize: %dx%d" % img.size, "\nMode: %s" % img.mode)
            print(spacer)
        except:
            print("\033[1;31;40m Unexpected error:\033[1;37;40m",
                  sys.exc_info()[0])
            raise
    return("Done making posters\033[1;33;40m o_O")


def main():
    print(make_posters.__doc__)
    print(make_posters())


if __name__ == "__main__":
    main()
