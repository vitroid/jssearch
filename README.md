# jssearch

[http://rs.luminousspice.com/hugo-site-search/](http://rs.luminousspice.com/hugo-site-search/)さんの、魔法のように高速な検索を使い、論文検索サイトを作成する。

## Final products

* `index.html` 検索画面。スマホで日本語変換した場合でもちゃんと検索できるようにすこしだけ改良した。
* `papers.css` Cascading style sheet
* `tn/` JPEGサムネイルの置き場。
* `pdf/` PDFの置き場
* `dist/` 本番サイト用データ

## Misc.

* `noimage-ls.png` サムネイルが作れなかった場合のプレイスホルダー。

## 改良した点

* [compositionend](https://developer.mozilla.org/ja/docs/Web/Reference/Events/compositionend)イベントをひろって、変換確定時にも検索結果を更新するようにした。
* 検索抜けが起こるバグを修正。
