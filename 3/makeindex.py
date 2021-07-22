#!/usr/bin/env python3
# coding: utf-8
from logging import getLogger
import sys
import json

# jssearchのためのインデックスを生成する。


logger = getLogger()

records = json.load(sys.stdin)


data = []
for id, rec in records.items():
    index = dict()
    # 講演番号
    # index["lab"] = rec["code"]
    # Session
    # index["ses"] = rec["code"][:rec["code"].find('-')]
    # reg id
    index["reg"] = id
    # 講演題目
    index["tit"] = rec["title"]
    # 講演者リスト
    index["spe"] = rec["authorlist"]
    # プレビュー画像
    index["pre"] = rec["tn"]
    # pdfファイル
    index["pdf"] = f"pdf/{id}.pdf"
    # 所属
    index["loc"] = "somewhere"
    # Type
    index["typ"] = "zoom"
    # 検索用文字列
    s = ""
    s += id + " "
    s += index["tit"] + " "
    s += index["spe"] + " "
    s += index["loc"] + " "
    s += rec["keyword3"] + " " # keyword1,2もできれば追加する。
    index["con"] = s
    data.append(index)
    # copy PDF files
    logger.info(index)

print(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True))
