leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

N = int(input())

for i in range(N):
    cont_led = 0
    V = input()
    for i in V:
        if i=="0":
            cont_led+=leds[0]
        elif i=="1":
            cont_led+=leds[1]
        elif i=="2":
            cont_led+=leds[2]
        elif i=="3":
            cont_led+=leds[3]
        elif i=="4":
            cont_led+=leds[4]
        elif i=="5":
            cont_led+=leds[5]
        elif i=="6":
            cont_led+=leds[6]
        elif i=="7":
            cont_led+=leds[7]
        elif i=="8":
            cont_led+=leds[8]
        elif i=="9":
            cont_led+=leds[9]
    print(f"{cont_led} leds")