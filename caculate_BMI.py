height = float(input("請輸入身高(公尺): "))
weight = float(input("請輸入體重(公斤): "))

answer = weight / height**2
print("BMI為: ", answer)

if answer < 18.5:
    print("體重過輕")
elif 18.5 <= answer < 24:
    print("正常範圍")
elif 24 <= answer < 27:
    print("過重")
elif 27 <= answer < 30:
    print("輕度肥胖")
elif 30 <= answer < 35:
    print("中度肥胖")
else:
    print("重度肥胖")