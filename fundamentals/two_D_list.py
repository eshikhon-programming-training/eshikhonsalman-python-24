a = [[1,3],[2,4]]
b = [[5,6],[7,8]]

sum_list = [[0,0],[0,0]]

for row in range(len(a)):
    # sum=0
    for col in range(len(a[row])):
       sum_list[row][col] = a[row][col] + b[row][col]
    #    sum_list.append(sum)
print(sum_list)