"""Repeating a beat in a loop."""

__author__ = "730319741"

beat: str = input("What beat do you want to repeat? ")
counter: int = 0
maximum: int = int(input("How many times do you want to repeat it? "))
oneBeat = str = beat

if maximum <= 0:
    print("No beat...")
else:
    while counter < maximum - 1:
        beat = beat + " " + oneBeat
        counter = counter + 1
        print(beat)
        
