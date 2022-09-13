#!/usr/bin/env python

import openpyxl
import os
from requests import get #requests package

table = openpyxl.load_workbook("/Users/matto/GoogleDrive/kensaku.xlsx")
sheet = table["kensaku"]


def escape(s):
    return s.replace('"', '\\"')


def download(url, file_name):
    # open in binary mode
    with open(file_name, "wb") as file:
        # get request
        response = get(url)
        # write to file
        file.write(response.content)

award=1
s = ""
for i,row in enumerate(sheet.rows):
    if i < 4:
        # header lines
        continue
    link, title, speakers = [col.value for col in row]
    if speakers == None:
        continue
    if link.find("=HYPERLINK")>=0:
        url, label = eval(link[10:])
    else:
        url, label = ("", link)
    if label == "受賞講演":
        label += str(award)
        award+=1
    preview = "{0}.jpg".format(label)
    localpdf = label+".pdf"
    if url is not "":
        if not os.path.exists(localpdf):
            download(url, localpdf)
        if not os.path.exists(preview):
            os.system("sips -s format jpeg {0} -Z 200 --out {1}".format(localpdf, preview))
    if not os.path.exists(preview):
        preview = "noimage.png"
    if url == "":
        pdflink = ""
    else:
        pdflink = "href='{0}'".format(url)
    s += """
{{
label: "{0}",
title: "{1}",
content: "{2}",
preview: "{3}",
pdflink: "{4}",
speakers: "{5}",
}},
""".format(label, escape(title), " ".join([label, speakers]), preview, pdflink, speakers)


s = "var data=[\n" + s + "]\n"
open("index2.js", "w").write(s)




    
    
