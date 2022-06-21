n1 = float(input("請輸入第1個數字: "))
s = input("請輸入+,-,*,/: ")
n2 = float(input("請輸入第2個數字: "))

if s == "+":
    print("答案為: ", n1 + n2)
elif s == "-":
    print("答案為: ", n1 - n2)
elif s == "*":
    print("答案為: ", n1 * n2)
elif s == "/":
    print("答案為: ", n1 / n2)
else:
    print("輸入錯誤，請重新輸入")