import random
print("0~2の整数を入力せよ[0:グー,1:チョキ,2:パー]")
cnt_w = 0
cnt_l = 0
cnt_d = 0
for i in range(3):
    you = 100
    while you >= 3:
        you = int(input("You:"))
        cpu = random.randint(0,2)
        print("CPU:",cpu,end = " ")
        if you==cpu:
            cnt_d += 1
            print("Draw!")
        elif (you+1)%3==cpu:
            cnt_w += 1
            print("You Win!")
        else:
            cnt_l += 1
            print("You Lose!")
print(f"{cnt_w}勝、{cnt_l}敗、{cnt_d}引き分け")