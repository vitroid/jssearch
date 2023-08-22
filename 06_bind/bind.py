# tab2excel
# applyの管理画面で生成した、タブ区切りプレーンテキストを読みこみ、錯討方式でフォーマットしてExcel出力

import csv
import glob
import json
import re
import sys
from logging import INFO, basicConfig, getLogger

import pypdf

# from pypdf.pdf import PageObject


def twoup(pages):
    """pagesを、2ページずつに束ねたpypdfページオブジェクトとしてyieldするiterator

    Args:
        pages (_type_): ページオブジェクトのリストまたはイテレータ
    """
    a4_width = 1190.5511811024 / 2
    a4_height = 841.8897637795

    for i, page in enumerate(pages):
        if i % 2 == 0:
            # A3 の台紙を生成
            base_page = pypdf.PageObject.create_blank_page(
                width=a4_width, height=a4_height
            )
            # A3の上にPDFを配置
            op = pypdf.Transformation().scale(0.656).translate(ty=a4_height / 2)
            page.add_transformation(op)
            page.mediabox.top += a4_height / 2
            page.mediabox.bottom += a4_height / 2
            base_page.merge_page(page)
        else:
            # op = pypdf.Transformation().translate(ty=a4_height / 2)
            op = pypdf.Transformation().scale(0.656).translate(ty=a4_height / 40)
            page.add_transformation(op)  # A3の下にPDFを配置
            base_page.merge_page(page, expand=False)

            yield base_page
            base_page = None

    if base_page is not None:
        yield base_page


basicConfig(level=INFO)
logger = getLogger()

files = glob.glob("../master/*.json")
db = dict()
rooms = dict()
for row, filename in enumerate(files):
    with open(filename) as f:
        data = json.load(f)
        code = data["code"]
        id = data["id"]
        m = re.search(r"[A-Za-z]+", code)
        if m is None:
            logger.warning((code, id))
        else:
            room = m.group()
            # logger.info((room, code, id))
            if code in db:
                logger.warning(f"same id: {id}, {db[code]}. Ignored.")
            else:
                db[code] = id
                if room not in rooms:
                    rooms[room] = []
                rooms[room].append(code)

# 部屋ごとに章分けする
# 引数で部屋が指定されたら、それらだけを再生成する
if len(sys.argv) > 1:
    roomlist = sys.argv[1:]
else:
    roomlist = rooms.keys()

for room in roomlist:
    writer = pypdf.PdfWriter()

    logger.info(f"{room}: {sorted(rooms[room])}")
    pages = []
    for code in sorted(rooms[room]):
        id = db[code]
        pdffile = f"../02_abstpdf/{id}/index.pdf"
        reader = pypdf.PdfReader(open(pdffile, "rb"))
        page = reader.pages[0]
        pages.append(page)
    for bound in twoup(pages):
        writer.add_page(bound)

    with open(f"{room}.pdf", "wb") as f:
        writer.write(f)


# workbook = Workbook(xlsx_file)
# worksheet = workbook.add_worksheet()
# # worksheet.write_rich_string(0, 0, 'hello', workbook.add_format({'font_script': 1}), 'world')
# # worksheet.write(1, 1, 'hello your world')
# # workbook.close()
# # sys.exit(0)

# patterns = {
#     "sup": workbook.add_format({"font_script": 1}),
#     "sub": workbook.add_format({"font_script": 2}),
# }

# # tab区切り形式で生成した管理画面データ。最初の2行にレコード順序が書かれている。
# field_order = "/Users/matto/Downloads/1658208630.tab"
# with open(field_order) as f:
#     read_tsv = csv.reader(f, delimiter="\t")

#     labels, fields = list(read_tsv)[:2]
#     for c, label in enumerate(labels):
#         if fields[c].find("array") == 0:
#             break
#         worksheet.write(0, c, label)

#     print(labels)
#     print(fields)

# if len(sys.argv) == 1:
#     files = glob.glob("../master/*.json")
# else:
#     files = [f"master/{i}.json" for i in sys.argv[1:]]

# for row, filename in enumerate(files):
#     with open(filename) as f:
#         data = json.load(f)
#         print(data)
#         for c, field in enumerate(fields):
#             if field.find("array") == 0:
#                 break
#             if field in data:
#                 col = data[field]
#                 if labels[c] in (
#                     "講演題目",
#                     "Title of the talk",
#                     "発表者リスト / List of authors",
#                 ):
#                     col = re.sub(r"<br />", "\n", col)
#                     cols = [col]
#                     # rich text化する??
#                     # https://xlsxwriter.readthedocs.io/example_rich_strings.html
#                     for htmltag, formatfunc in patterns.items():
#                         # colsの各要素をどんどん展開して、長いリストにする。
#                         newcols = []
#                         for col in cols:
#                             if type(col) is str:
#                                 regexp = f"<{htmltag}.*?>(.*?)</{htmltag}>"
#                                 m = re.split(regexp, col)
#                                 ## 奇数番目の前にfuncを挿入する。
#                                 m2 = []
#                                 for j, e in enumerate(m):
#                                     if j % 2 == 1:
#                                         m2.append(formatfunc)
#                                     m2.append(e)
#                                 newcols += m2
#                             else:
#                                 newcols.append(col)
#                         cols = newcols
#                         # print(cols)
#                     newcols = []
#                     for col in cols:
#                         if col != "":
#                             newcols.append(col)
#                     cols = newcols
#                     print(cols)
#                     if len(cols) > 0:
#                         if len(cols) == 1:
#                             worksheet.write(row + 1, c, cols[0])
#                         else:
#                             worksheet.write_rich_string(row + 1, c, *cols)
#                 elif col != "":
#                     worksheet.write(row + 1, c, col)
#     # worksheet.write_row(row, 0, data)

# # Closing the xlsx file.
# worksheet.write_rich_string(0, 0, "test")
# workbook.close()
