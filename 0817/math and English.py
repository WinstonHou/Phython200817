math = int(input("數學:"))
english = int(input("英文:"))
if math >=0 and math<=100 and english >=0 and english<=100:
    if math>=90 and english>=90:
        print("有獎品")
    elif math <60 and english<60:
        print("你會被懲罰")
    elif math<60 or english<60:
        print("再加油")
else:
        print("error")
