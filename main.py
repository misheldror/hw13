import my_func
from my_func import print_stars

for _ in range(5):
    my_func.print_stars()
print()
for _ in range(5):
    print_stars()
print()

help(my_func.print_stars)