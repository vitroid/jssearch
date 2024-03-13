#!/usr/bin/env python

import pandas as pd
import glob
import os
from slugify import slugify
from pathlib import Path


def pdfname(authors, year, title):
    # author
    aus = [au.split(" ")[0] for au in authors.split(",")]
    if len(aus) == 1:
        au = aus[0]
    elif len(aus) == 2:
        au = aus[0] + " and " + aus[1]
    else:
        au = aus[0] + " et al."

    # title
    for head in range(2, 12):
        # 段々長くしていく。
        tis = title.replace(":", " -").split(" ")[-head:]
        # paperpile nomenclature
        ti = " ".join(tis).replace("/", " - ").replace("?", "")

        initial = au[0]

        # Finder is in English mode
        name = f"/Users/matto/Google Drive/My Drive/Paperpile/All Papers/{initial}/{au} {year} - *{ti}.pdf".replace(
            " ", "[ ]"
        )
        # Finder is in Japanese mode
        name = f"/Users/matto/Google Drive/マ*/Paperpile/All Papers/{initial}/{au} {year} - *{ti}.pdf".replace(
            " ", "[ ]"
        )

        files = glob.glob(name)
        if len(files) < 2:
            break
        # if len(files) > 1:
        #     print(
        #         f"Ambiguity in the first {head} words of the title {au} {year} - {ti}"
        #     )

    # print(name, files)
    if len(files) == 1:
        return files[0]
    print(f"Missing {name}")
    print(title)
    return None


frame = pd.read_csv("papers.csv")
frame = frame.rename(columns={"Publication year": "Year"})
# 加工なしでjsで表示できるデータ構造が望ましい。
# 検索専用のフィールドにabstractを含める。

# 新しい列を作る。
# print(frame.columns)
# print(frame.loc[:, ["Authors", "Title", "Journal", "Volume", "Pages", "Year"]])
frame["Publication"] = [
    f"<span class='jo'>{row.Journal}</span> <span class='vo'>{row.Volume}</span>, {row.Pages} ({row.Year})."
    for row in frame.itertuples()
]
frame["context"] = [
    f"{row.Authors} {row.Title} {row.Publication} {row.DOI} {row.Abstract}"
    for row in frame.itertuples()
]
frame["PDF"] = ["noimage-ls.png" for row in frame.itertuples()]
frame["tn"] = ["noimage-ls.png" for row in frame.itertuples()]
for i, row in enumerate(frame.itertuples()):
    path = pdfname(row.Authors, row.Year, row.Title)
    if path is not None:
        basename = slugify(Path(path).stem)
        try:
            os.symlink(path, f"pdf/{basename}.pdf")
        except FileExistsError:
            pass
        # print(f"pdf/{basename}")
        frame.loc[i, "PDF"] = f"pdf/{basename}.pdf"
        frame.loc[i, "tn"] = f"tn/{basename}.jpg"
    else:
        frame.loc[i, "context"] += " (no PDF)"

frame = frame.rename(
    columns={"Authors": "au", "Title": "ti", "Publication": "pu", "context": "con"}
)
data = frame.sort_values(by="Year", ascending=False).loc[
    :, ["au", "ti", "pu", "DOI", "con", "tn", "PDF"]
]
with open("papers.js", "w") as f:
    f.write("data=")
    data.to_json(f, orient="records", indent=True)
# 複雑な検索条件は実装しない。あくまでgrepベースで検索する。その代わり、チェックを入れたものをカートにほりこめるようにする。