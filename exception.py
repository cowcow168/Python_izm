#例外処理の例


#簡単な足し算を行う関数

# def exception_addition_test(value_1,value_2):
#     print('====計算開始====')
#     result = 0
#
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算が出来ませんでした。')
#     finally:
#         print('計算終了')
#     return result
#
# print(exception_addition_test(100,200))
# print(exception_addition_test(100,'200'))


#規模が大きめのアプリケーションを作成している場合
#呼び出し元にエラーを上げ、そのエラー処理を任せる時の書き方

# def exception_addition_test(value_1,value_2):
#     print('====計算開始====')
#     result = 0
#
#     try:
#         result = value_1 + value_2
#     except:
#         print('計算が出来ませんでした。')
#         raise
#     finally:
#         print('計算終了')
#     return result
#
# #tryの中でtryを使用しているイメージ。(エラー)発生時にraiseするように記述しているので、呼び出し元のtryへ伝播
# try:
#     print(exception_addition_test(100,200))
#     print(exception_addition_test(200,200))
#     print(exception_addition_test(100,'200'))
# except:
#     print('エラーを受け取りました。')


#エラー内容(スタックトレース)の取得
# 処理を実行中にエラーが発生すると、例外内容（スタックトレース）が標準出力へ出力されます。
# それをプログラム側で取得することも可能

import sys
import traceback

def exception_addition_test(value_1,value_2):
    print('====計算開始====')
    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算が出来ませんでした。')
        raise
    finally:
        print('計算終了')
    return result

try:
    print(exception_addition_test(100,'200'))
except:
    print('--------------------------------')
    print(traceback.format_exc(sys.exc_info()[2]))
    print('--------------------------------')
