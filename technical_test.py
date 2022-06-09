
# Name = Isaiah Ikharona
# Problem = Technical test question 3.

def houses_in_line(n):
    def steal_from_house(index):
        if index >= len(n):
            return 0
        else:
            return max(n[index] + steal_from_house(index + 2), steal_from_house(index + 1))

    return steal_from_house(0)

line_1 = houses_in_line([2, 5, 1, 3, 6, 2, 4])
line_2 = houses_in_line([2, 10, 14, 8, 1])

print("Maximum possible money that can be stolen from houses in line 1 = ", line_1)

print("Maximum possible money that can be stolen from houses in line 2 = ", line_2)

