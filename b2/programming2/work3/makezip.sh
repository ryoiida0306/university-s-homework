#!/bin/bash

# 作業用（提出）ファイル名を決定
curdir=`pwd`
curdir=`basename $curdir`
dirname=$curdir-`whoami`-`date +%F-%T`
orig_list=`ls`

# コピーを作成
mkdir $dirname
cp -R $orig_list $dirname
touch $dirname/.$dirname

# いらないファイルを削除
make -C $dirname clean

# code 変更 UTF8, LFへ
find $dirname -name \*java | xargs -L1 nkf -w -Lu --overwrite
# makefileも
find $dirname -name Makefile | xargs -L1 nkf -w -Lu --overwrite
# Explainも
nkf -w -Lu --overwrite Explain.txt

# code をインデント
find $dirname -name \*java | xargs -L1 astyle --style=java

# zipで固める
zip -r ../$dirname.zip $dirname

# 作業ディレクトリ削除
rm -rf $dirname
