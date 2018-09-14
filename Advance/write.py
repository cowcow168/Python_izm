import sys
print(sys.stdin.encoding)

#UTF-8は最初から多言語での記述を前提とされているので、インターネットのように世界中からアクセスされるようなサイトの記述
fin_sjis = open('read.txt', 'r', encoding='utf-8')
#EUC-JPはUnix系OSで扱われるだけでなく日本語を前提
fout_euc = open('euc-jp.txt', 'w', encoding='euc_jp')
fout_utf = open('utf-8.txt', 'w', encoding='utf-8')

for row in fin_sjis:
    fout_euc.write(row)
    fout_utf.write(row)

fin_sjis.close()
fout_euc.close()
fout_utf.close()