# tab2excel
# applyの管理画面で生成した、タブ区切りプレーンテキストを読みこみ、錯討方式でフォーマットしてExcel出力

import csv
import glob
import json
import re
import sys

from xlsxwriter.workbook import Workbook

xlsx_file = 'contents.xlsx'

workbook = Workbook(xlsx_file)
worksheet = workbook.add_worksheet()
# worksheet.write_rich_string(0, 0, 'hello', workbook.add_format({'font_script': 1}), 'world')
# worksheet.write(1, 1, 'hello your world')
# workbook.close()
# sys.exit(0)

patterns = {"sup": workbook.add_format({'font_script': 1}),
            "sub": workbook.add_format({'font_script': 2}),}

# tab区切り形式で生成した管理画面データ。最初の2行にレコード順序が書かれている。
field_order = "/Users/matto/Downloads/1658208630.tab"
with open(field_order) as f:
    read_tsv = csv.reader(f, delimiter ='\t')

    labels, fields = list(read_tsv)[:2]
    for c, label in enumerate(labels):
        if fields[c].find("array") == 0:
            break
        worksheet.write(0, c, label)

    print(labels)
    print(fields)

if len(sys.argv) == 1:
    files = glob.glob("../master/*.json")
else:
    files = [f"master/{i}.json" for i in sys.argv[1:]]

for row, filename in enumerate(files):
    with open(filename) as f:
        data = json.load(f)
        print(data)
        for c, field in enumerate(fields):
            if field.find("array") == 0:
                break
            if field in data:
                col = data[field]
                if labels[c] in ("講演題目", "Title of the talk", "発表者リスト / List of authors"):
                    col = re.sub(r'<br />', '\n', col)
                    cols = [col]
                    # rich text化する??
                    # https://xlsxwriter.readthedocs.io/example_rich_strings.html
                    for htmltag, formatfunc in patterns.items():
                        # colsの各要素をどんどん展開して、長いリストにする。
                        newcols = []
                        for col in cols:
                            if type(col) is str:
                                regexp = f'<{htmltag}.*?>(.*?)</{htmltag}>'
                                m = re.split(regexp, col)
                                ## 奇数番目の前にfuncを挿入する。
                                m2 = []
                                for j, e in enumerate(m):
                                    if j % 2 == 1:
                                        m2.append(formatfunc)
                                    m2.append(e)
                                newcols += m2
                            else:
                                newcols.append(col)
                        cols = newcols
                        # print(cols)
                    newcols = []
                    for col in cols:
                        if col != "":
                            newcols.append(col)
                    cols = newcols
                    print(cols)
                    if len(cols) > 0:
                        if len(cols) == 1:
                            worksheet.write(row+1, c, cols[0])
                        else:
                            worksheet.write_rich_string(row+1, c, *cols)
                elif col != "":
                    worksheet.write(row+1, c, col)
    # worksheet.write_row(row, 0, data)

# Closing the xlsx file.
worksheet.write_rich_string(0, 0, 'test')
workbook.close()
