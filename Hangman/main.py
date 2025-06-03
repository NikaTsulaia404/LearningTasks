import random

animals = ['dog', 'cat', 'mouse', 'baboon']

lives = 6
gamocnoba = random.choice(animals)
print("Sityva aris", len(gamocnoba), "asosgan.")

display = ""
for letter in gamocnoba:
    display += "_"

print(display)

while display != gamocnoba:
    gamoicani_aso = input("Sheiyvanet erti aso: \n").lower()

    if gamoicani_aso not in gamocnoba:
        lives -= 1
        print(f"Tqven dagakldat 1 sicocxle! Darchenilia {lives}")

        if lives == 0:
            print(f"Tqven agargaqvt sicocxle darchenili! Sityva iyo: {gamocnoba}\nTamashi waaget!")
            break

    nateli_display = ""
    for index in range(len(gamocnoba)):
        if gamocnoba[index] == gamoicani_aso:
            nateli_display += gamoicani_aso
        else:
            nateli_display += display[index]

    display = nateli_display
    print(display)

if display == gamocnoba:
    print(f"Gilocav, gamoicani sityva: {gamocnoba}")
