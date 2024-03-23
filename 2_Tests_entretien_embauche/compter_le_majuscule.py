def count_upper_char1(str):
    count = 0
    for i in str:
        if i.isupper():
            count += 1
    return count


def count_upper_char2(str):
    l = [1 if c.isupper() else 0 for c in str]
    count = sum(l)
    return count


def count_upper_char3(str):
    return len([1 for c in str if c.isupper()])


s = "Bonjour TotO"
print(count_upper_char1(s))
print(count_upper_char2(s))
print(count_upper_char3(s))
