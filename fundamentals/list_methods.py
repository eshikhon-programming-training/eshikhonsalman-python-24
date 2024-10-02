a = [1,2,3]

print("Before append",a)
a.append('hello')
# a[len(a):] = [4]
print("After append",a)
# a[:] = []
# print("After Clear",a)
b = a.copy()
print("After Copy",b)

fruits = [4, 55, 64, 32, 16, 32,'orange']
x = fruits.index(32)
print("after index",x)
fruits.insert(1, "orange")
print("after insert",fruits)

fruits.pop(2)

print("After Pop", fruits)

fruits.remove("orange")

print("After Remove",fruits)



fruits.reverse()

print("After Reverse",fruits)

c = [1,10,-1,1.5]
c.sort()
# c.sort(reverse=True)
print("After Sort",c)

