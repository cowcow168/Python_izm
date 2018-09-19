python_list = []
python_list.append(100)
python_list.append(200)
python_list.append(10)
python_list.append(800)
python_list.append(60)

#リスト自体をソートする(更新させる)
print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

python_list.sort()

print('---------------------------------')
print('【ソート表示】')
for value in python_list:
    print(value)

#リストのソート結果を取得する

print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

print('---------------------------------')
print('【ソート表示】')
for value in sorted(python_list):
    print(value)

print('---------------------------------')
print('【リストの再表示】')
for value in python_list:
    print(value)

#リスト自体を逆順にする
# python_list = []
# python_list.append('python')
# python_list.append('izm')
# python_list.append('sample')
# python_list.append('list')
# python_list.append('reversed')
#
# print('---------------------------------')
# print('【そのまま表示】')
# for value in python_list:
#     print(value)
#
# python_list.reverse()
#
# print('---------------------------------')
# print('【逆順表示】')
# for value in python_list:
#     print(value)

#リストのソート結果を逆順で取得する
python_list = []
python_list.append('python')
python_list.append('izm')
python_list.append('sample')
python_list.append('list')
python_list.append('reversed')

print('---------------------------------')
print('【そのまま表示】')
for value in python_list:
    print(value)

print('---------------------------------')
print('【逆順表示】')
for value in reversed(python_list):
    print(value)

print('---------------------------------')
print('【逆順表示 スライスで実行】')
for value in python_list[::-1]:
    print(value)

print('---------------------------------')
print('【リストの再表示】')
for value in python_list:
    print(value)