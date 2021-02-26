#!/usr/bin/env python

# 履歴書の業績目録をhtmlで生成する。

import pandas as pd
import glob
import os
from slugify import slugify
from pathlib import Path

frame = pd.read_csv("papers-mm.csv")
frame = frame.rename(columns={'Publication year': 'Year'})
frame["Authors"] = [row.Authors.replace(",", ", ") for row in frame.itertuples()]

frame["Publication"] = [f"<p>{row.Title}. {row.Authors}. <i>{row.Journal}</i> <b>{row.Volume}</b> {row.Pages} ({row.Year}). DOI:{row.DOI}</p>".replace("Matsumoto M", "<u>Matsumoto M</u>") for row in frame.itertuples()]
for i, row in enumerate(frame.sort_values("Year").itertuples()):
    print(row.Publication)
