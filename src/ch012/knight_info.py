import sys
from knight import Knight

for name in sys.argv[1:]:
    k = Knight(name)
    print(f"Name: {k._title} {name}")
    print(f"Favorite Color: {k._favorite_color}")
    print(f"Quest: {k._quest}")
    print(f"Comment: {k._comment}")
    print()

