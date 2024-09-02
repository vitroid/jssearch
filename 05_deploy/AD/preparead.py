# prepare advertisements page
import json
import shutil
import sys
from subprocess import STDOUT, TimeoutExpired, check_output

ads = {
    "ad-1": [
        ["マイクロトラック・ベル株式会社", "https://www.microtrac.com/jp/"],
    ],
    "ad-2": [
        ["BCSJ Chem. Lett.", "https://www.journal.csj.jp/journal/cl"],
    ],
    "ad-3": [
        ["ブルカージャパン株式会社", "https://www.bruker.com/ja.html"],
    ],
    "ad-4": [
        ["株式会社リガク", "https://japan.rigaku.com/ja"],
    ],
    "ad-5": [
        ["株式会社ブライト", "https://bright-jp.com"],
    ],
    "ad-6": [
        ["株式会社ユニソク", "https://www.unisoku.co.jp"],
    ],
    "ad-7": [
        ["ビー・エー・エス株式会社", "https://bas.co.jp"],
    ],
    "ad-8": [
        ["旭化学工業株式会社", "http://www.chem-asahi.co.jp"],
    ],
    "ad-9": [
        ["Royal Society of Chemistry", "https://rsc.li/Dalton"],
    ],
    "ad-10": [
        ["BCSJ Chem. Lett.", "https://www.journal.csj.jp/journal/cl"],
    ],
}


def main():
    js = []
    for ad in ads:
        rec = dict()

        # make tn
        pdf = f"{ad}.pdf"
        dst = f"tn/{ad}.jpg"
        cmd = [
            "sips",
            "-s",
            "format",
            "jpeg",
            # "--cropToHeightWidth", f"{wh}", f"{wh}",
            "-z",
            "297",
            "210",
            f"{pdf}",
            "--out",
            f"../{dst}",
        ]
        output = check_output(cmd)
        rec["tn"] = dst

        dst2 = f"pdf/{ad}.pdf"
        shutil.copyfile(pdf, "../" + dst2)
        rec["pdf"] = dst2

        sponsors = []
        for sp in ads[ad]:
            name, url = sp
            sponsors.append({"url": url, "name": name})
        rec["sp"] = sponsors
        js.append(rec)
    print(json.dumps(js, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
