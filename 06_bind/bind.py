import glob
import re
import sys
from logging import INFO, basicConfig, getLogger
import os
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

# files = glob.glob("../master/*.json")
files = glob.glob("../05_deploy/pdf/*.pdf")

rooms = dict()
for filename in files:
    code = os.path.splitext(os.path.basename(filename))[0]
    # 日付と部屋で章分けする
    m = re.search(r"^[A-Za-z0-9]+", code)
    if m is None:
        logger.warning(code)
    else:
        room = m.group()
        # logger.info((room, code, id))
        if room not in rooms:
            rooms[room] = []
        rooms[room].append(code)

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
        pdffile = f"../05_deploy/pdf/{code}.pdf"
        reader = pypdf.PdfReader(open(pdffile, "rb"))
        page = reader.pages[0]
        pages.append(page)
    if room.find("Aw") >= 0 or room.find("S") == 0:
        for bound in pages:
            writer.add_page(bound)
    else:
        for bound in twoup(pages):
            writer.add_page(bound)

    with open(f"{room}.pdf", "wb") as f:
        writer.write(f)

    with open(f"makefile.{room}", "w") as f:
        f.write(f"{room}.pdf: ")
        for code in sorted(rooms[room]):
            pdffile = f"../05_deploy/pdf/{code}.pdf"
            f.write(pdffile + " ")
        f.write(f"\n\tpython3 bind.py {room}\n")
