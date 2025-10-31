temperatures = [23.5, 25.4, 27.6, 24.9, 26.7, 24.6]

min= temperatures[0]
max=temperatures[0]
total = 0
n = 0

for element in temperatures :

    if element > max :

        max = element

    elif element < min :

        min = element

    total += element
    n += 1



moyenne= total/n




print(f"Températures : { temperatures }")
print(f"          min: { min }")
print(f"          max: { max }")
print(f"     moyenne : { moyenne } ")
print(f" nb. mesures : { n } ")


