#ジェネレーターを作成する(リストで作成したものをループで回す時は、最初に容量を食うが、
# ジェネレータ(反復可能なオブジェクト)を作成すると作成するまでは、待機状態になるので容量の節約になる

#通常の関数
def func_sample():
    print('おはよう')
    print('こんにちは')
    print('こんばんは')

#ジェネレーターを使用
def func_sample():
    yield('おはよう')
    yield('こんにちは')
    yield('こんばんは')
func_sample()
#上記では、当然printされなくなったが、すでにジェネレーター(関数)になっている。

# for i in func_sample():
#     print(i)
#
# f= func_sample()
# print(next(f))
# print(next(f))
# print(f.next())

gen_sample = (i for i in 'おはよう こんにちは こんばんは'.split())

print(gen_sample)
for i in gen_sample:
    print(i)