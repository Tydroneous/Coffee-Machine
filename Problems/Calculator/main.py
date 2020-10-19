first = float(input())
second = float(input())
third = input()

if (second == 0) and (third == "div") or (second == 0) and (third == "mod") or (second == 0) and (third == "/"):
    print("Division by 0!")
elif third == "mod":
    print(first % second)
elif third == "pow":
    print(pow(first, second))
elif third == "div":
    print(first // second)
elif third == "+":
    print(first + second)
elif third == "-":
    print(first - second)
elif third == "*":
    print(first * second)
elif third == "/":
    print(first / second)

# else:
#     print(eval((str(first)) + third + str(second)))
