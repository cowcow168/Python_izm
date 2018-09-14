#名前のない関数の作成(無名関数,匿名関数)

def plus_value(num_1,num_2):
    return num_1 + num_2

print(plus_value(10,100))

l_func = lambda num_1,num_2: num_1 + num_2
print(plus_value(10,100))