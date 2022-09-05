# jssearch

[http://rs.luminousspice.com/hugo-site-search/](http://rs.luminousspice.com/hugo-site-search/)さんの、魔法のように高速な検索を使い、錯体討論会の検索サイトを作成する。

## データ加工工程(2022)

n.makefileで順番に処理を行う。2022の方針として、jsonをできるだけ分割しておくことで、Makeによる並列化を最大限活用できるようにする。

0. sync
1. Cleanse
    1. 受付サイトからダウンロードした16xxxxx.jsonからpre.jsonを作る。(自動処理、重複申請のフィルタリング)
    2. master.jsonの生成(pre.jsonから手でエディット)
    3. data.jsonの生成()
2. ABSTRACT PDFの生成
3. (?)
4. Program編成用PDFの生成。ここまで動けば、プログラム編成班にタスクを渡せる。
5. 講演番号を追加
6. search用のindexを生成、tnへのリンクを追加
7. シンポジウムと受賞講演を統合。(Sympoの中での準備が要る)
8. 講演番号つきPDFの生成 →続いて2に戻る。
9. (none)
10. Add ads.
11.
12.
13. svelteへのデータ反映とdeploy

## ToDo (2022)

* Excelのカラム番号とカラム題名の対応表を生成するだけのボタンがほしい。←tabでチェックなしでダウンロードすればいい。
* Excelダウンロード機能の廃止
* Excelファイルはプログラム編成班に直接ダウンロードさせず、こちらのもっているmasterデータベースでの修正を反映したものから生成することにする。リッチテキストの処理もその時に行う。

## Final productsv

* `index.html` 検索画面。スマホで日本語変換した場合でもちゃんと検索できるようにすこしだけ改良した。
* `cjscc70.css` Cascading style sheet
* `tn/` JPEGサムネイルの置き場。
* `p/` ファイル名をMD5化したPDFの置き場
* `riis/` 本番サイト用データ
* `chem/` バックアップサイト用データ

## Misc.

* (`content.html` 予稿集画面。indexに統合)
* `noimage.png` サムネイルが作れなかった場合のプレイスホルダー。
* `Sympo/sympo.py` シンポジウムのインデックスを生成し、同時にPDFをunlabelledフォルダに移す。
* `Award/award.py` 受賞講演のインデックスを生成する。予稿のサイズが違うので、ラベルは手作業で貼った。
* `addlabel.py` unlabelled/にあるPDFにラベルを付け、pdf/に入れる。
  * `2020.js` 通常講演のインデックス。www.chem上のmakeindex2020.pyで生成したものをもってくる。
  * `Award/award.js` 受賞講演のインデックス。Award/award.pyで生成。
  * `Sympo/sympo.js` シンポジウムのインデックス。Sympo/sympo.pyで生成する。
  * `index.js` 上の3つを統合し、PDFの所在を別サーバ上へのリンクに変更したもの。merge.pyで作成する。
* `replacer.py` サイトごとの固有設定を生成し、履歴を残す。
* `unlabelled/` ラベルなしのPDF置き場。
* `pdf/` ラベルありのPDF置き場。
* setting.yaml Gitには上げられない情報。

## 改良した点

* [compositionend](https://developer.mozilla.org/ja/docs/Web/Reference/Events/compositionend)イベントをひろって、変換確定時にも検索結果を更新するようにした。
* 検索抜けが起こるバグを修正。

## 今後の改良

* データとコードの分離。イベント固有のコードをなくし、データのみからカスタムページを生成できるようにする。
* 前処理の段数を減らす。
* 頑強化。
* 認証方法の改善。
