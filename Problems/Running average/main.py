numbers = input()
my_num = []
for i in range(len(numbers) - 1):
    my_num.append((int(numbers[i]) + (int(numbers[i+1]))) / 2)


print(my_num)
