# prepare advertisements page
import json
import shutil
import sys
from subprocess import STDOUT, TimeoutExpired, check_output

ads = {
    "ad_1":   [["アジレント・テクノロジー株式会社", "https://www.chem-agilent.com"],],
    "ad_2":   [["株式会社アントンパール・ジャパン", "https://www.anton-paar.com/jp-jp/"],],
    "ad_3":   [["株式会社セルシステム", "http://www.cellsystem.co.jp/"],],
    "ad_4":   [["株式会社島津製作所", "https://www.shimadzu.co.jp"],],
    "ad_5":   [["株式会社東陽テクニカ", "https://www.toyo.co.jp"],],
    "ad_6":   [["株式会社ブライト", "https://bright-jp.com"],],
    "ad_7":   [["株式会社UNICO", "https://www.glovebox.co.jp"],],
    "ad_8":   [["株式会社ユニソク", "https://www.unisoku.co.jp"],],
    "ad_9":   [["株式会社リガク", "https://japan.rigaku.com/ja"],],
    "ad_10":  [["田中貴金属工業株式会社", "https://gold.tanaka.co.jp/index.php"],],
    "ad_11":  [["福岡酸素株式会社", "https://fksanso.co.jp"],],
    "ad_12":  [["ブルカージャパン株式会社", "https://www.bruker.com/ja.html"],],
    "ad_13":  [["マイクロトラック・ベル株式会社", "https://www.microtrac.com/jp/"],],
    "ad_14":  [["株式会社新興精機", "https://shinkouseiki.co.jp"],
                ["桜木理化学機械株式会社", "http://www.sakuragi-rk.co.jp"],],
    "ad_15":  [["三共出版株式会社", "https://www.sankyoshuppan.co.jp"],
                ["", ""]],
}


def main():
    js = []
    for ad in ads:
        rec = dict()

        # make tn
        pdf = f"{ad}.pdf"
        dst = f"tn/{ad}.jpg"
        cmd = ["sips",
               "-s", "format", "jpeg",
        #"--cropToHeightWidth", f"{wh}", f"{wh}",
               "-z", "297", "210",
               f"{pdf}",
               "--out", f"../{dst}"]
        output = check_output(cmd)
        rec["tn"] = dst

        dst2 = f"pdf/{ad}.pdf"
        shutil.copyfile(pdf, "../"+dst2)
        rec["pdf"] = dst2

        sponsors = []
        for sp in ads[ad]:
            name, url = sp
            sponsors.append({"url":url, "name":name})
        rec["sp"] = sponsors
        js.append(rec)
    print(json.dumps(js, sort_keys=True, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
