#with文の使い方を覚える(ファイルを取り扱う時に使用する)
#前処理と後処理とするオブジェクトを扱う時に簡易的な構文で使用できる。

with open('file.txt') as f:
    #
    # 何らかの処理を行う
    #

    print(f.closed)
print(f.closed)

#後処理として、ファイルをクローズしてくれる

f = open('file.txt')

try:
    #
    # 何らかの処理を行う
    #
    pass
except:
    pass
finally:
    f.close()