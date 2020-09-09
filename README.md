jssearch

[http://rs.luminousspice.com/hugo-site-search/](http://rs.luminousspice.com/hugo-site-search/)さんの、魔法のように高速な検索を使い、錯体討論会の検索サイトを作成する。

* `index.html` 検索画面。スマホで日本語変換した場合でもちゃんと検索できるようにすこしだけ改良した。
* `content.html` 予稿集画面。
* `tinyweb.py` ローカルに実行するためのwebサーバー。8087ポートを使用。
* `noimage.png` サムネイルが作れなかった場合のプレイスホルダー。
* `Sympo/sympo.py` シンポジウムのインデックスを生成し、同時にPDFをunlabelledフォルダに移す。
* `Award/award.py` 受賞講演のインデックスを生成する。予稿のサイズが違うので、ラベルは手作業で貼った。
* `addlabel.py` unlabelled/にあるPDFにラベルを付け、pdf/に入れる。
  * `2020.js` 通常講演のインデックス。www.chem上のmakeindex2020.pyで生成したものをもってくる。
  * `Award/award.js` 受賞講演のインデックス。Award/award.pyで生成。
  * `Sympo/sympo.js` シンポジウムのインデックス。Sympo/sympo.pyで生成する。
  * `index.js` 上の3つを統合し、PDFの所在を別サーバ上へのリンクに変更したもの。merge.pyで作成する。
* `unlabelled/` ラベルなしのPDF置き場。
* `pdf/` ラベルありのPDF置き場。
* `tn/` JPEGサムネイルの置き場。
* `p/` ファイル名をMD5化したPDFの置き場
* setting.yaml Gitには上げられない情報。
## 改良した点

* [compositionend](https://developer.mozilla.org/ja/docs/Web/Reference/Events/compositionend)イベントをひろって、変換確定時にも検索結果を更新するようにした。
