# prepare advertisements page
import json
import shutil
import sys
from subprocess import STDOUT, TimeoutExpired, check_output

ads = {
    "ad_1": [
        ["スペクトリス株式会社", "https://www.malvernpanalytical.com/jp"],
    ],
    "ad_2": [
        ["BCSJ Chem. Lett.", "https://www.journal.csj.jp/journal/cl"],
    ],
    "ad_3": [
        ["株式会社ブライト", "https://bright-jp.com"],
    ],
    "ad_4": [
        ["ブルカージャパン株式会社", "https://www.bruker.com/ja.html"],
    ],
    "ad_5": [
        ["マイクロトラック・ベル株式会社", "https://www.microtrac.com/jp/"],
    ],
    "ad_6": [
        ["株式会社ユニソク", "https://www.unisoku.co.jp"],
    ],
    "ad_7_1": [
        ["Royal Society of Chemistry", "https://rsc.li/Dalton"],
    ],
    "ad_7_2": [
        ["Royal Society of Chemistry", "https://rsc.li/frontiers-inorganic"],
    ],
    "ad_89": [
        ["HPCシステムズ株式会社", "https://www.hpc.co.jp"],
        ["日本分光株式会社", "http://www.jasco.co.jp/jpn/home/index.html"],
    ],
    "ad_1011": [
        ["ブルカージャパン株式会社", "https://www.bruker.com/ja.html"],
        [
            "有限会社ラブディポット",
            "https://www.google.com/maps/place/3-chōme-14-7+Yokokawa/@35.7053719,139.8121558,18.82z/data=!4m7!3m6!1s0x60188ed5454e1473:0xd0ab6fcd36d4730e!4b1!8m2!3d35.7054771!4d139.8132035!16s%2Fg%2F11clnn4b78?entry=ttu",
        ],
    ],
    "ad_12": [
        ["株式会社リガク", "https://japan.rigaku.com/ja"],
    ],
    #
    #
    # "ad_1":   [["アジレント・テクノロジー株式会社", "https://www.chem-agilent.com"],],
    # "ad_2":   [["株式会社アントンパール・ジャパン", "https://www.anton-paar.com/jp-jp/"],],
    # "ad_3":   [["株式会社セルシステム", "http://www.cellsystem.co.jp/"],],
    # "ad_4":   [["株式会社島津製作所", "https://www.shimadzu.co.jp"],],
    # "ad_5":   [["株式会社東陽テクニカ", "https://www.toyo.co.jp"],],
    #     "ad_7":   [["株式会社UNICO", "https://www.glovebox.co.jp"],],
    # "ad_9":   [["株式会社リガク", "https://japan.rigaku.com/ja"],],
    # "ad_10":  [["田中貴金属工業株式会社", "https://gold.tanaka.co.jp/index.php"],],
    # "ad_11":  [["福岡酸素株式会社", "https://fksanso.co.jp"],],
    # "ad_14":  [["株式会社新興精機", "https://shinkouseiki.co.jp"],
    #             ["桜木理化学機械株式会社", "http://www.sakuragi-rk.co.jp"],],
    # "ad_15":  [["三共出版株式会社", "https://www.sankyoshuppan.co.jp"],
    #             ["", ""]],
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
