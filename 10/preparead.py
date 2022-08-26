# prepare advertisements page
import sys
from subprocess import STDOUT, check_output, TimeoutExpired
import json
import shutil

ads = {
    "ad_2":  [["Excillum AB", "https://www.excillum.com/"],],
    "ad_3":  [["株式会社リガク", "https://japan.rigaku.com/ja"],],
    "ad_4":  [["ブルカージャパン株式会社", "http://www.bruker.co.jp/"],],
    "ad_5":  [["株式会社セルシステム", "http://www.cellsystem.co.jp/"],],
    "ad_6":  [["三進金属工業株式会社", "https://www.sanshinkinzoku.co.jp/"],],
    "ad_7":  [["大研科学産業株式会社", "https://daiken-kagaku.co.jp/"],],
    "ad_8":  [["日産化学株式会社", "https://www.nissanchem.co.jp/"],],
    "ad_9":  [["株式会社アズバイオ", "http://www.azbio.co.jp/"],
    ["竹田理化工業株式会社", "http://www.takeda-rika.co.jp/"],],
    "ad_10": [["ナカライテスク株式会社", "https://www.nacalai.co.jp/"],
    ["日本分析工業株式会社", "https://www.jai.co.jp/"],],
    "ad_11": [["八洲薬品株式会社", "http://www.yashimachem.co.jp/"],
    ["株式会社安田商店", "https://yasuda-sci.com/"],],
    "ad_12": [["株式会社ヤップ", "https://yap-paradise.com/"],],
}


def main():
    js = []
    for ad in ads:
        rec = dict()

        # make tn
        pdf = f"AD/{ad}.pdf"
        dst = f"tn/{ad}.jpg"
        cmd = ["sips",
               "-s", "format", "jpeg",
        #"--cropToHeightWidth", f"{wh}", f"{wh}",
               "-z", "297", "210",
               f"{pdf}",
               "--out", f"{dst}"]
        output = check_output(cmd)
        rec["tn"] = dst

        dst2 = f"pdf/{ad}.pdf"
        shutil.copyfile(pdf, dst2)
        rec["pdf"] = dst2

        sponsors = []
        for sp in ads[ad]:
            name, url = sp
            sponsors.append({"url":url, "name":name})
        rec["sp"] = sponsors
        js.append(rec)
    print(json.dumps(js, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
