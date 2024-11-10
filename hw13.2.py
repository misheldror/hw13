#a
students: int = int(input('enter students number: '))
left: int = students % 30
classes: int = students // 30
print(f'left: {left}')
print(f'classes: {classes}')

#b
num: int = int(input('enter a number: '))
while 10 > num or num > 99:
    num: int = int(input('enter a number: '))
else:
    ahadot: int = num % 10
    asarot: int = num // 10

if ahadot > asarot:
    print(f'{ahadot}{asarot}')
else:
    print(num)

#c
prime: list[int] = []
divider: int = 2
for i in range(200):
    if i % divider == 0 and i > divider:
        divider += 1
        continue
    else:
        prime.append(i)
print(prime)