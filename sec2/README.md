## 10
[l10](./l10.py)
## 11
## 問題
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

### 解法
- cat ./popular-names.txt | tr '\t' ' ' > ./[ans11.txt](ans11.txt)
- [sed](https://qiita.com/tori_taro/items/7fa8a34c1bd94d89ac28)
- [expand](https://atmarkit.itmedia.co.jp/ait/articles/1611/02/news023.html#sample1) ...？？

## 12
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

- [l12](./l12.py)

## 13
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

- [l13](./l13.py)

## 14
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

-[l14](./l14.py)
## 15
