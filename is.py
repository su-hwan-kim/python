# is 는 변수의 Object가 같을때 True를 return

a = []
b = []
c = a

result = (a is b)
print("a is b ?", result)

result = (a is c)
print("a is c ?", result)

result = (b is c)
print("b is c ?", result)

# == 는 변수의 Volue가 같을때 True를 return

d = []
e = []
f = d

result = (d == e)
print("d == e ?", result)

result = (d == f)
print("d == f ?", result)

result = (e == f)
print("e == f ?", result)
