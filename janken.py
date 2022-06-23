import random
print("0~2の整数を入力せよ[0:グー,1:チョキ,2:パー]")
for i in range(3):
    you = 100
    while you >= 3:
        you = int(input("You:"))
        cpu = random.randint(0,2)
        print("CPU:",cpu,end = " ")
        if you==cpu:
            print("Draw!")
        elif (you+1)%3==cpu:
            print("You Win!")
        else:
            print("You Lose!")