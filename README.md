jssearch

[http://rs.luminousspice.com/hugo-site-search/](http://rs.luminousspice.com/hugo-site-search/)さんの、魔法のように高速な検索を使い、錯体討論会の検索サイトを作成する。

* `dumpxls.py` 討論会の講演PDFの所在の含まれるxlsファイルから、サムネイル画像と、インデックスファイルを生成するスクリプト。
* `search.html` 検索画面。スマホで日本語変換した場合でもちゃんと検索できるようにすこしだけ改良した。
* `tinyweb.py` ローカルに実行するためのwebサーバー。8087ポートを使用。
* `noimage.png` サムネイルが作れなかった場合のプレイスホルダー。

## 改良した点

* [compositionend](https://developer.mozilla.org/ja/docs/Web/Reference/Events/compositionend)イベントをひろって、変換確定時にも検索結果を更新するようにした。



