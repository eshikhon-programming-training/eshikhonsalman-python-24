main_value = "hello world"

value = list(main_value)
print(value)
# value = ['h','e','l','l','o']
vowels = ['a','e','i','o','u']
count = 0
# for i in value:
#     if i in vowels:
#         print("i is vowel")
#         count+=1
#     else:
#         print("i is a consonant")
count = 0
for i in vowels:
    count += value.count(i)
print(count)