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
files = sorted(glob.glob("../03_sheetpdf/genpdf/*/index.pdf"))

writer = pypdf.PdfWriter()
for filename in files:
    reader = pypdf.PdfReader(open(filename, "rb"))
    page = reader.pages[0]
    writer.add_page(page)
    # else:
    #     for bound in twoup(pages):
    #         writer.add_page(bound)

with open(f"sheet.pdf", "wb") as f:
    writer.write(f)
