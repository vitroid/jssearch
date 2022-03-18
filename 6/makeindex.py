#!/usr/bin/env python3
# coding: utf-8
from logging import getLogger
import sys
import json
from hashlib import md5

# jssearchのためのインデックスを生成する。

# converted from preview.js
def authorlists(record):
    speakermark = "〇"
    if record["award.apply"]:
        speakermark = "◎"
    elif record["award2.apply"]:
        speakermark = "★"

    namesj = []
    namese = []

    namej = record["happyo.name"]
    namee = record["happyo.namee"]

    if record["happyo.speak"]:
        namej = speakermark + namej
        namee = speakermark + namee

    affil = record["happyo.affil"]
    namej += "<sup>"+affil+"</sup>"
    namee += "<sup>"+affil+"</sup>"

    namesj.append(namej)
    namese.append(namee)

    for i in range(1, int(record["array.count"])+1):
        namej = record[f"array.{i}happyo.name"]
        namee = record[f"array.{i}happyo.namee"]
        if namee == "":
            break

        if record[f"array.{i}happyo.speak"]:
            namej = speakermark + namej
            namee = speakermark + namee

        affil = record[f"array.{i}happyo.affil"]
        namej += "<sup>"+affil+"</sup>"
        namee += "<sup>"+affil+"</sup>"

        namesj.append(namej)
        namese.append(namee)

    auj = "・".join(namesj)
    aue = ", ".join(namese)

    affilsj = []
    affilse = []

    for i in range(1,11):
        affilj = record[f"affil{i}"]
        affile = record[f"affil{i}e"]
        if not affile:
            break
        affilsj.append(f"<sup>{i}</sup>{affilj}")
        affilse.append(f"<sup>{i}</sup>{affile}")

    auj = "(" + "・".join(affilsj) + f") {auj}"
    aue = "(" + ", ".join(affilse) + f") {aue}"

    return auj, aue


logger = getLogger()
# setting = yaml.load(open("setting.yaml"), Loader=yaml.SafeLoader)
setting = json.load(open("setting.json"))
salt = setting["salt"]
logger.error(salt)

records = json.load(sys.stdin)



data = []
for id, rec in records.items():
    index = dict()
    code = rec["code"]
    index["lab"] = code
    # Session
    index["ses"] = code[:code.find('-')]
    # reg id
    index["reg"] = id
    # 講演者情報
    # 講演者リスト
    auj, aue = authorlists(rec)
    if rec["style"] in "13":
        index["inf"] = [rec["title"], auj, rec["titlee"], aue]
    else:
        index["inf"] = [rec["titlee"], aue]
    # プレビュー画像
    index["pre"] = f"tn/{code}.jpg" # rec["tn"]
    # pdfファイル
    index["pdf"] = f"pdf/{code}.pdf"

    # Search keys
    index["sea"] = rec["keyword3"]

    key = index["lab"]
    salty = salt+key
    # index["md5"] = md5(salty.encode()).hexdigest()


    data.append(index)
    # copy PDF files
data = sorted(data, key=lambda x: x["lab"])

print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
