# Trouver les mots commun entre deux phrases

def get_common_words(str1, str2):
    str1_array = str1.lower().replace(",", "").split(' ')
    str2_array = str2.lower().replace(",", "").split(' ')
    common_words = []
    
    for w in str1_array:
        if w in str2_array and not w in common_words:
            common_words.append(w)
    
    return common_words


# with set
def get_common_words2(str1, str2):
    str1_array = set(str1.lower().replace(",", "").split(' '))
    str2_array = set(str2.lower().replace(",", "").split(' '))
    common_words = []
    # first method
    # return list(str1_array.intersection(str2_array))
    # second method
    return list(str1_array & str2_array)


s1 = "Bonjour je m'appelle Herman"
s2 = "bonjour, je suis Hmak"

print(get_common_words(s1, s2))
print(get_common_words2(s1, s2))
