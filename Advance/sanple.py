# https://qiita.com/tag1216/items/e1e3c565a2bf8dbc7f86
#キーターのアドヴェントチャレンジの記事に掲載されているもの

import time
from contextlib import contextmanager
from collections import defaultdict
#下記は、コマンドラインで実行する時にTrueになるので実行される。それ以外のimportなどで読み込まれた時は、処理されない
#ちょっと試験的にテストしたい時に使用する(値をprintして確認したい時など)
# if __name__ == '__main__':
#     start = time.time()
#     for i in range(0,11):
#         print("a")
#     elapsed_time = time.time() -start
#     print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

# 下記は、通常の書き方
#計測したい処理
# :
# start = time.time()
# end = time.time()
# print(end - start)


#例題1　以下の様に２つある処理を別々に計測したい場合を考えてみます。
# 処理内容はダミーとして指定時間スループするだけにします。
#処理1
# time.sleep(0.1)
#
# #処理2
# time.sleep(0.2)


# start = time.time()
#
# #処理1
#
# time.sleep(0.1)
#
# end = time.time()
# print('処理1:{:.3f}'.format(end-start))
#
# start = time.time()
#
# #処理2
#
# time.sleep(0.2)
#
# end = time.time()
# print('処理2:{:.3f}'.format(end-start))
#時間計測のコードが混ざるので元々やっていた処理がわかりにくくなってしまいます。




##############################################################################
# コンテキストマネージャーで書いた場合
# コンテキストマネージャーを使うことで、時間計測のコードを計測対象のコードから分離して定義
##############################################################################

# @contextmanager
# def simple_timer(label):
#     start = time.time()
#     yield
#     end = time.time()
#     print('{}: {:.3f}'.format(label,end-start))
#
# #計測したい範囲の処理を囲んであげる。
# with simple_timer('処理1'):
#     time.sleep(0.1)
#
# with simple_timer('処理2'):
#     time.sleep(0.2)

##############################################################################
# 次は、先ほどのコードが繰り返し呼ばれる場合に、２つの処理を別々に集計して計測したい場合
#下みたいなイメージ
##############################################################################

# for _ in range(10):
#     # 処理1
#     time.sleep(0.1)
#     # 処理2
#     time.sleep(0.2)

# times = defaultdict(float)
#
# for _ in range(10):
#     start = time.time()
#
#     # 処理1
#     time.sleep(0.1)
#
#     end = time.time()
#     times['処理1'] += end - start
#
#     start = time.time()
#
#     # 処理2
#     time.sleep(0.2)
#
#     end = time.time()
#     times['処理2'] += end - start
#
# for label, t in times.items():
#     print('{}: {:.3f}'.format(label, t))

##############################################################################
# コンテキストマネージャーで書いた場合
# コンテキストマネージャーではyield文で呼び出し元に値を渡すことができる。
##############################################################################

# @contextmanager
# def sum_timer():
#
#     times = defaultdict(float)
#
#     @contextmanager
#     def timer(label):
#         start = time.time()
#         yield
#         end = time.time()
#         times[label] += end - start
#
#     yield timer
#
#     for label, t in times.items():
#         print('{}: {:.3f}'.format(label, t))

#呼び出し側ではwith文の後ろのasでyieldから渡された値を受け取ること
# with sum_timer() as timer:
#
#     for _ in range(10):
#
#         with timer('処理1'):
#             time.sleep(0.1)
#
#         with timer('処理2'):
#             time.sleep(0.2)

##############################################################################
# コンテキストマネージャーで書いた場合
# 全体の処理時間を出したい
##############################################################################

@contextmanager
def total_timer(total_label):

    times = defaultdict(float)

    @contextmanager
    def timer(label):
        start = time.time()
        yield
        end = time.time()
        times[label] += end - start

    with timer(total_label):
        yield timer

    for label, t in times.items():
        if label != total_label:
            print('{}:{:.3f}'.format(label,t))
        print('{}: {:.3f}'.format(total_label, t))

with total_timer('全体') as timer:

    for _ in range(10):

        with timer('処理1'):
            time.sleep(0.1)

        with timer('処理2'):
            time.sleep(0.2)