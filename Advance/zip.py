#!/usr/bin/env python

import sys
import zipfile

#エラー処理も何も考えていないので、単純に第一引数のzipファイルがSJISのファイルをもっていると思って展開しているだけ
# TODO 上記を解消するスクリプトを追加する
def main(filename):
    with zipfile.ZipFile(filename) as zip:
        for info in zip.infolist():
            info.filename = info.filename.decode('shift-jis').encode('utf-8')
            zip.extract(info)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))