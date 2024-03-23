# Inverser une chaine(Reverse)
def reverse_string(str):
    r = ""
    for i in str:
        r = i + r
    return r


def reverse_string_with_slice(str):
    return str[-1::-1]


s = "Bonjour toto"
print(reverse_string(s))
print(reverse_string_with_slice(s))
