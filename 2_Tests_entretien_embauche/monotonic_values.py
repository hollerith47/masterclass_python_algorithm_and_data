# Monotonic data or values
# increasing
# decreasing

def is_increasing_monitonic_values1(l):
    for i in range(len(l) - 1):
        if l[i + 1] < l[i]:
            return False
    return True


def is_increasing_monitonic_values2(l):
    return l == sorted(l)


a = [1, 5, 6, 9, 11, 11, 12, 15]
b = [1, 5, 6, 6, 5, 7, 10]

print("a :", is_increasing_monitonic_values1(a))
print("b :", is_increasing_monitonic_values1(b))
print()
print("a :", is_increasing_monitonic_values2(a))
print("b :", is_increasing_monitonic_values2(b))
