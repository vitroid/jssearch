SHELL=/bin/bash
MASTER=../master

# 個人情報などを、別の場所にまとめることにした。
# PRIVATE=/Users/matto/Library/CloudStorage/GoogleDrive-vitroid@gmail.com/My\ Drive/00Priority/2023錯討73
PRIVATE=../private

# 改行符入りのJSONが壊れている。これはPerlの問題か。
JSON=$(PRIVATE)/1724828732.json
sync:
	rsync -av reg@www.chem.okayama-u.ac.jp:reg2/var/projects/apply/attach ..



prepare_master: $(JSON) decompose.py
	-mkdir $(MASTER)
	python decompose.py $< $(MASTER)

# 2023 メール送信前に、内容を修正したレコードを洗いだす。
# 修正内容をreg2に戻すことも考えたのだが、
# 結局、安全にDBを書換えるのは困難と判断する。(改行文字の扱いが非常に不安)
# なので、英語と日本語の題名が逆になっていても何が間違っていても、メール送信時には反映させないことにする。
# これまで通り、講演番号だけをデータベースに追加して、それを通知する。
verify: $(JSON) verify.py
	python verify.py $< $(MASTER)


# テストのために、DBをこちらに写しておく。
# sync_db:
# 	rsync -av reg@www.chem.okayama-u.ac.jp:reg2/var/projects/apply/DB ..
